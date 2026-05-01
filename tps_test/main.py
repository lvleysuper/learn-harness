"""
TPS测试主入口
"""
import asyncio
import argparse
import sys
import io
from pathlib import Path
from typing import List

# 加载项目根目录的 .env 文件
from dotenv import load_dotenv
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from tps_test.config import Config, BenchmarkType, Language
from tps_test.clients import OpenAIClient
from tps_test.benchmarks import HumanEvalBenchmark
from tps_test.prompts import CodeGenerationPrompt
from tps_test.evaluators import CodeExecutor
from tps_test.utils import TestResult, calculate_statistics
from tps_test.reporters import ConsoleReporter


async def run_single_test(
    client: OpenAIClient,
    problem,
    config: Config,
    executor: CodeExecutor,
    debug: bool = False
) -> TestResult:
    prompt = CodeGenerationPrompt.create_prompt(problem, config.benchmark.language.value)
    
    response = await client.generate(
        prompt=prompt,
        max_tokens=config.api.max_tokens,
        temperature=config.api.temperature
    )
    
    if not response.success:
        return TestResult(
            problem_id=problem.problem_id,
            success=False,
            tokens=0,
            elapsed=response.elapsed,
            tps=0,
            error=response.error or "Unknown error"
        )
    
    if debug:
        print(f"\n=== {problem.problem_id} 生成的代码 ===")
        print(response.content[:500])
        print("=" * 50)
    
    test_code = None
    passed_tests = False
    execution_error = None
    
    if problem.test_cases:
        test_code = problem.test_cases[0]
        full_code = f"{response.content}\n{test_code}"
        try:
            exec_result = executor.execute(full_code, "python", timeout=10)
            passed_tests = exec_result.success
            if not exec_result.success and debug:
                execution_error = exec_result.error
                print(f"执行错误: {exec_result.error[:300]}")
        except Exception as e:
            passed_tests = False
            if debug:
                print(f"异常: {str(e)}")
    
    return TestResult(
        problem_id=problem.problem_id,
        success=True,
        tokens=response.tokens,
        elapsed=response.elapsed,
        tps=response.tps,
        passed_tests=passed_tests
    )


async def run_tests(config: Config, debug: bool = False) -> List[TestResult]:
    client = OpenAIClient(
        api_key=config.api.api_key,
        api_base_url=config.api.api_base_url,
        model=config.api.model,
        timeout=config.api.timeout
    )
    
    benchmark = HumanEvalBenchmark(language=config.benchmark.language.value)
    problems = benchmark.get_problems(
        problem_ids=config.benchmark.problem_ids,
        limit=config.benchmark.num_problems
    )
    
    executor = CodeExecutor()
    results: List[TestResult] = []
    
    print(f"开始测试: {len(problems)} 个问题, 并发数: {config.test.concurrency}")
    print(f"模型: {config.api.model}")
    print(f"基准测试: {config.benchmark.benchmark_type.value}")
    print("-" * 70)
    
    semaphore = asyncio.Semaphore(config.test.concurrency)
    
    async def limited_test(idx, problem):
        async with semaphore:
            result = await run_single_test(client, problem, config, executor, debug)
            ConsoleReporter.print_progress(idx + 1, len(problems), result)
            return result
    
    tasks = [limited_test(i, p) for i, p in enumerate(problems)]
    results = await asyncio.gather(*tasks)
    
    await client.close()
    
    return results


def parse_args():
    parser = argparse.ArgumentParser(description="AI代码生成TPS测试工具")
    
    parser.add_argument(
        "--num-problems", "-n",
        type=int,
        default=10,
        help="测试问题数量 (默认: 10)"
    )
    
    parser.add_argument(
        "--concurrency", "-c",
        type=int,
        default=2,
        help="并发请求数 (默认: 2)"
    )
    
    parser.add_argument(
        "--model", "-m",
        type=str,
        default="glm-5",
        help="模型名称 (默认: glm-5)"
    )
    
    parser.add_argument(
        "--api-key", "-k",
        type=str,
        default=None,
        help="API密钥 (也可通过环境变量API_KEY设置)"
    )
    
    parser.add_argument(
        "--api-base-url", "-u",
        type=str,
        default=None,
        help="API基础URL"
    )
    
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=1024,
        help="最大生成Token数 (默认: 1024)"
    )
    
    parser.add_argument(
        "--language", "-l",
        type=str,
        choices=["python", "cpp", "javascript", "java"],
        default="python",
        help="编程语言 (默认: python)"
    )
    
    parser.add_argument(
        "--skip-execution",
        action="store_true",
        help="跳过代码执行验证"
    )
    
    parser.add_argument(
        "--debug",
        action="store_true",
        help="显示生成的代码内容（调试模式）"
    )
    
    return parser.parse_args()


def main():
    args = parse_args()
    
    config = Config.from_env()
    
    if args.api_key:
        config.api.api_key = args.api_key
    if args.api_base_url:
        config.api.api_base_url = args.api_base_url
    if args.model:
        config.api.model = args.model
    if args.max_tokens:
        config.api.max_tokens = args.max_tokens
    
    config.benchmark.num_problems = args.num_problems
    config.benchmark.language = Language(args.language)
    config.test.concurrency = args.concurrency
    
    debug = args.debug
    
    if not config.api.api_key:
        print("错误: 请设置API_KEY环境变量或通过 --api-key 参数提供")
        sys.exit(1)
    
    results = asyncio.run(run_tests(config, debug))
    stats = calculate_statistics(results)
    
    ConsoleReporter.print_results(results, stats)


if __name__ == "__main__":
    main()