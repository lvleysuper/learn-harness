"""
API客户端基类
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
import time


@dataclass
class APIResponse:
    success: bool
    content: str
    elapsed: float
    tokens: int = 0
    prompt_tokens: int = 0
    total_tokens: int = 0
    status_code: int = 200
    error: Optional[str] = None
    tps: float = 0.0

    def __post_init__(self):
        if self.elapsed > 0 and self.tokens > 0:
            self.tps = self.tokens / self.elapsed


class BaseClient(ABC):
    def __init__(self, api_key: str, api_base_url: str, model: str, timeout: float = 120.0):
        self.api_key = api_key
        self.api_base_url = api_base_url.rstrip("/")
        self.model = model
        self.timeout = timeout

    @abstractmethod
    async def generate(self, prompt: str, max_tokens: int = 1024, temperature: float = 0.0) -> APIResponse:
        """生成代码"""
        pass

    @abstractmethod
    async def close(self):
        """关闭客户端"""
        pass