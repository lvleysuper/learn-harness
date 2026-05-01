"""
简化版 TPS 测试脚本
"""
import asyncio
import time
import statistics
import os
from pathlib import Path
from typing import List
import httpx
import sys
import io

# 加载项目根目录的 .env 文件
from dotenv import load_dotenv
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

API_BASE_URL = os.getenv("API_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1")
API_KEY = os.getenv("API_KEY", "")

async def make_request(client: httpx.AsyncClient, prompt: str = "请写一段200字左右的中文内容，介绍人工智能的发展历史。") -> dict:
    start_time = time.time()
    try:
        response = await client.post(
            f"{API_BASE_URL}/chat/completions",
            json={
                "model": "glm-5",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 500,
            },
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
            timeout=120.0,
        )
        elapsed = time.time() - start_time

        if response.status_code == 200:
            data = response.json()
            usage = data.get("usage", {})
            completion_tokens = usage.get("completion_tokens", 0)
            prompt_tokens = usage.get("prompt_tokens", 0)
            total_tokens = usage.get("total_tokens", 0)

            if completion_tokens == 0:
                content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
                completion_tokens = len(content)

            return {
                "status_code": response.status_code,
                "elapsed": elapsed,
                "tokens": completion_tokens,
                "prompt_tokens": prompt_tokens,
                "total_tokens": total_tokens,
                "success": completion_tokens > 0,
                "tps": completion_tokens / elapsed if elapsed > 0 else 0,
            }
        else:
            return {
                "status_code": response.status_code,
                "elapsed": elapsed,
                "tokens": 0,
                "success": False,
                "error": f"HTTP {response.status_code}: {response.text[:200]}",
                "tps": 0,
            }
    except Exception as e:
        return {
            "status_code": 0,
            "elapsed": time.time() - start_time,
            "tokens": 0,
            "success": False,
            "error": str(e),
            "tps": 0,
        }

async def test_tps(num_requests: int = 5, concurrency: int = 2):
    if not API_KEY:
        print("请设置API_KEY环境变量")
        return

    print(f"Token Per Second 测试: {num_requests}个请求, 并发数: {concurrency}")
    print("-" * 50)

    results: List[dict] = []

    async with httpx.AsyncClient() as client:
        semaphore = asyncio.Semaphore(concurrency)

        async def limited_request(idx):
            async with semaphore:
                result = await make_request(client)
                status = "OK" if result["success"] else f"FAIL: {result.get('error', '')[:50]}"
                print(f"请求 {idx+1}/{num_requests}: {result['tokens']} tokens, {result['tps']:.1f} tps, {result['elapsed']:.2f}s - {status}")
                return result

        start_time = time.time()
        tasks = [limited_request(i) for i in range(num_requests)]
        results = await asyncio.gather(*tasks)
        total_time = time.time() - start_time

    successful = [r for r in results if r["success"]]
    failed = [r for r in results if not r["success"]]

    print("-" * 50)
    print(f"总请求数: {num_requests}")
    print(f"成功请求: {len(successful)}")
    print(f"失败请求: {len(failed)}")
    print(f"总耗时: {total_time:.2f}秒")

    if successful:
        total_tokens = sum(r["tokens"] for r in successful)
        tps_values = [r["tps"] for r in successful]
        avg_tps = statistics.mean(tps_values)
        overall_tps = total_tokens / total_time

        print(f"\n=== Token 生成速度 ===")
        print(f"总生成Token数: {total_tokens}")
        print(f"单请求平均TPS: {avg_tps:.1f} tokens/秒")
        print(f"整体TPS: {overall_tps:.1f} tokens/秒")
        print(f"TPS中位数: {statistics.median(tps_values):.1f} tokens/秒")
        if len(tps_values) >= 3:
            print(f"TPS标准差: {statistics.stdev(tps_values):.1f} tokens/秒")

        latencies = [r["elapsed"] for r in successful]
        print(f"\n=== 延迟统计 ===")
        print(f"平均延迟: {statistics.mean(latencies):.2f}秒")
        print(f"最小延迟: {min(latencies):.2f}秒")
        print(f"最大延迟: {max(latencies):.2f}秒")

    if failed:
        print(f"\n失败请求详情:")
        for i, r in enumerate(failed[:3]):
            print(f"  失败{i+1}: {r.get('error', 'unknown')}")

if __name__ == "__main__":
    num_requests = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    concurrency = int(sys.argv[2]) if len(sys.argv) > 2 else 2

    asyncio.run(test_tps(num_requests, concurrency))