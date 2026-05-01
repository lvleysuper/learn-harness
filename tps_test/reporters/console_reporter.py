"""
控制台报告生成器
"""
from typing import List
from tps_test.utils.stats import TestResult, Statistics, calculate_statistics


class ConsoleReporter:
    @staticmethod
    def print_results(results: List[TestResult], stats: Statistics):
        print("\n" + "=" * 70)
        print(" TPS 测试报告 - 代码生成性能")
        print("=" * 70)
        
        print(f"\n总请求数: {stats.total_requests}")
        print(f"成功请求: {stats.successful_requests}")
        print(f"失败请求: {stats.failed_requests}")
        print(f"测试通过率: {stats.pass_rate:.1f}%")
        
        if stats.successful_requests > 0:
            print("\n" + "-" * 70)
            print(" Token 生成速度 (TPS)")
            print("-" * 70)
            print(f"  平均 TPS:     {stats.avg_tps:>10.1f} tokens/秒")
            print(f"  中位数 TPS:   {stats.median_tps:>10.1f} tokens/秒")
            print(f"  整体 TPS:     {stats.overall_tps:>10.1f} tokens/秒")
            print(f"  最小 TPS:     {stats.min_tps:>10.1f} tokens/秒")
            print(f"  最大 TPS:     {stats.max_tps:>10.1f} tokens/秒")
            if stats.std_tps > 0:
                print(f"  标准差:       {stats.std_tps:>10.1f} tokens/秒")
            
            print("\n" + "-" * 70)
            print(" 延迟统计")
            print("-" * 70)
            print(f"  平均延迟:     {stats.avg_latency:>10.2f} 秒")
            print(f"  最小延迟:     {stats.min_latency:>10.2f} 秒")
            print(f"  最大延迟:     {stats.max_latency:>10.2f} 秒")
            
            print("\n" + "-" * 70)
            print(" Token 统计")
            print("-" * 70)
            print(f"  总生成 Token: {stats.total_tokens:>10d}")
            print(f"  总耗时:       {stats.total_time:>10.2f} 秒")
        
        print("\n" + "-" * 70)
        print(" 详细结果")
        print("-" * 70)
        print(f"{'问题ID':<15} {'状态':<8} {'Tokens':<10} {'TPS':<12} {'延迟(s)':<10} {'测试':<8}")
        print("-" * 70)
        
        for r in results:
            status = "成功" if r.success else "失败"
            test_status = "通过" if r.passed_tests else "未通过"
            tps_str = f"{r.tps:.1f}" if r.success else "-"
            latency_str = f"{r.elapsed:.2f}" if r.success else "-"
            tokens_str = str(r.tokens) if r.success else "-"
            
            print(f"{r.problem_id:<15} {status:<8} {tokens_str:<10} {tps_str:<12} {latency_str:<10} {test_status:<8}")
        
        if stats.failed_requests > 0:
            print("\n" + "-" * 70)
            print(" 失败详情")
            print("-" * 70)
            for r in results:
                if not r.success:
                    print(f"  {r.problem_id}: {r.error[:80]}")
        
        print("\n" + "=" * 70)
    
    @staticmethod
    def print_progress(current: int, total: int, result: TestResult):
        status = "成功" if result.success else "失败"
        test_status = "通过" if result.passed_tests else "未通过"
        tps_str = f"{result.tps:.1f}" if result.success else "-"
        
        print(f"[{current}/{total}] {result.problem_id}: {status} | {result.tokens} tokens | {tps_str} tps | 测试: {test_status}")