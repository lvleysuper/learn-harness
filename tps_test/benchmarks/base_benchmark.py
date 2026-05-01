"""
基准测试基类
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional, Any


@dataclass
class Problem:
    problem_id: str
    description: str
    prompt: str
    language: str
    test_cases: List[Any]
    entry_point: Optional[str] = None
    canonical_solution: Optional[str] = None
    difficulty: Optional[str] = None
    tags: Optional[List[str]] = None


class BaseBenchmark(ABC):
    def __init__(self, language: str = "python"):
        self.language = language
        self._problems: List[Problem] = []
    
    @abstractmethod
    def load(self) -> List[Problem]:
        """加载测试问题"""
        pass
    
    def get_problems(self, problem_ids: Optional[List[str]] = None, limit: Optional[int] = None) -> List[Problem]:
        """获取测试问题"""
        if not self._problems:
            self._problems = self.load()
        
        problems = self._problems
        
        if problem_ids:
            problems = [p for p in problems if p.problem_id in problem_ids]
        
        if limit:
            problems = problems[:limit]
        
        return problems
    
    @abstractmethod
    def get_test_code(self, problem: Problem, generated_code: str) -> str:
        """生成测试代码"""
        pass