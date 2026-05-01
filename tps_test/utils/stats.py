"""
统计工具
"""
import statistics
from dataclasses import dataclass
from typing import List


@dataclass
class TestResult:
    problem_id: str
    success: bool
    tokens: int
    elapsed: float
    tps: float
    passed_tests: bool = False
    error: str = ""


@dataclass
class Statistics:
    total_requests: int
    successful_requests: int
    failed_requests: int
    total_tokens: int
    total_time: float
    avg_tps: float
    overall_tps: float
    median_tps: float
    std_tps: float
    min_tps: float
    max_tps: float
    avg_latency: float
    min_latency: float
    max_latency: float
    pass_rate: float = 0.0


def calculate_statistics(results: List[TestResult]) -> Statistics:
    successful = [r for r in results if r.success]
    failed = [r for r in results if not r.success]
    passed = [r for r in results if r.passed_tests]
    
    total_tokens = sum(r.tokens for r in successful)
    total_time = sum(r.elapsed for r in successful)
    
    tps_values = [r.tps for r in successful] if successful else [0]
    latencies = [r.elapsed for r in successful] if successful else [0]
    
    avg_tps = statistics.mean(tps_values) if tps_values else 0
    median_tps = statistics.median(tps_values) if tps_values else 0
    std_tps = statistics.stdev(tps_values) if len(tps_values) > 1 else 0
    min_tps = min(tps_values) if tps_values else 0
    max_tps = max(tps_values) if tps_values else 0
    
    overall_tps = total_tokens / total_time if total_time > 0 else 0
    
    pass_rate = len(passed) / len(results) * 100 if results else 0
    
    return Statistics(
        total_requests=len(results),
        successful_requests=len(successful),
        failed_requests=len(failed),
        total_tokens=total_tokens,
        total_time=total_time,
        avg_tps=avg_tps,
        overall_tps=overall_tps,
        median_tps=median_tps,
        std_tps=std_tps,
        min_tps=min_tps,
        max_tps=max_tps,
        avg_latency=statistics.mean(latencies) if latencies else 0,
        min_latency=min(latencies) if latencies else 0,
        max_latency=max(latencies) if latencies else 0,
        pass_rate=pass_rate
    )