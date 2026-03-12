import asyncio
import random
from typing import List
from vectormesh.models import QueryRequest, SearchResult
from vectormesh.adapters.base import BaseAdapter

class MockAdapter(BaseAdapter):
    def __init__(self, name: str, latency_range: tuple = (0.01, 0.05)):
        self.name = name
        self.latency_range = latency_range

    async def search(self, request: QueryRequest) -> List[SearchResult]:
        await asyncio.sleep(random.uniform(*self.latency_range))
        
        return [
            SearchResult(
                id=f"{self.name}-{i}",
                score=1.0 - (i * 0.05),
                metadata={"source": self.name, "index": i}
            )
            for i in range(request.top_k)
        ]

    async def health_check(self) -> bool:
        return True
