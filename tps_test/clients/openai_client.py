"""
OpenAI兼容API客户端
"""
import httpx
from typing import Optional
from .base_client import BaseClient, APIResponse


class OpenAIClient(BaseClient):
    def __init__(self, api_key: str, api_base_url: str, model: str, timeout: float = 120.0):
        super().__init__(api_key, api_base_url, model, timeout)
        self._client: Optional[httpx.AsyncClient] = None

    async def _get_client(self) -> httpx.AsyncClient:
        if self._client is None:
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