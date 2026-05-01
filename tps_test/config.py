"""
配置管理模块
"""
import os
from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum


class BenchmarkType(Enum):
    HUMANEVAL = "humaneval"
    MBPP = "mbpp"
    CUSTOM = "custom"


class Language(Enum):
    PYTHON = "python"
    CPP = "cpp"
    JAVASCRIPT = "javascript"
    JAVA = "java"
    TYPESCRIPT = "typescript"


@dataclass
class APIConfig:
    api_base_url: str = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    api_key: str = field(default_factory=lambda: os.getenv("API_KEY", ""))
    model: str = "glm-5"
    max_tokens: int = 1024
    temperature: float = 0.0
    timeout: float = 120.0


@dataclass
class BenchmarkConfig:
    benchmark_type: BenchmarkType = BenchmarkType.HUMANEVAL
    language: Language = Language.PYTHON
    problem_ids: Optional[List[int]] = None
    num_problems: int = 10
    difficulty: Optional[str] = None


@dataclass
class TestConfig:
    num_requests: int = 10
    concurrency: int = 2
    warmup_requests: int = 1
    retry_on_failure: bool = True
    max_retries: int = 3


@dataclass
class Config:
    api: APIConfig = field(default_factory=APIConfig)
    benchmark: BenchmarkConfig = field(default_factory=BenchmarkConfig)
    test: TestConfig = field(default_factory=TestConfig)
    output_format: str = "console"

    @classmethod
    def from_env(cls) -> "Config":
        config = cls()
        config.api.api_key = os.getenv("API_KEY", config.api.api_key)
        config.api.api_base_url = os.getenv("API_BASE_URL", config.api.api_base_url)
        config.api.model = os.getenv("MODEL", config.api.model)
        return config