"""
OpenAI兼容API客户端
"""
import httpx
import os
from typing import Optional
from .base_client import BaseClient, APIResponse


class OpenAIClient(BaseClient):
    def __init__(self, api_key: str, api_base_url: str, model: str, timeout: float = 120.0, disable_proxy: bool = True):
        super().__init__(api_key, api_base_url, model, timeout)
        self._client: Optional[httpx.AsyncClient] = None
        self.disable_proxy = disable_proxy

    async def _get_client(self) -> httpx.AsyncClient:
        if self._client is None:
            # 禁用系统代理，避免代理连接问题
            if self.disable_proxy:
                # 清除代理环境变量
                proxy_vars = ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy']
                for var in proxy_vars:
                    os.environ.pop(var, None)
                self._client = httpx.AsyncClient(timeout=self.timeout, proxy=None)
            else:
                self._client = httpx.AsyncClient(timeout=self.timeout)
        return self._client

    async def generate(self, prompt: str, max_tokens: int = 1024, temperature: float = 0.0) -> APIResponse:
        import time
        start_time = time.time()
        
        try:
            client = await self._get_client()
            response = await client.post(
                f"{self.api_base_url}/chat/completions",
                json={
                    "model": self.model,
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": max_tokens,
                    "temperature": temperature,
                },
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
            )
            elapsed = time.time() - start_time
            
            if response.status_code == 200:
                data = response.json()
                usage = data.get("usage", {})
                content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
                
                completion_tokens = usage.get("completion_tokens", 0)
                if completion_tokens == 0:
                    completion_tokens = len(content)
                
                return APIResponse(
                    success=len(content) > 0,
                    content=content,
                    elapsed=elapsed,
                    tokens=completion_tokens,
                    prompt_tokens=usage.get("prompt_tokens", 0),
                    total_tokens=usage.get("total_tokens", 0),
                    status_code=response.status_code,
                )
            else:
                return APIResponse(
                    success=False,
                    content="",
                    elapsed=elapsed,
                    status_code=response.status_code,
                    error=f"HTTP {response.status_code}: {response.text[:200]}",
                )
        except Exception as e:
            return APIResponse(
                success=False,
                content="",
                elapsed=time.time() - start_time,
                status_code=0,
                error=str(e),
            )

    async def close(self):
        if self._client:
            await self._client.aclose()
            self._client = None