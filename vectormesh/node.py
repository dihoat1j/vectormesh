import time
from typing import List
from vectormesh.models import QueryRequest, SearchResult
from vectormesh.adapters.base import BaseAdapter

class VectorNode:
    def __init__(self, id: str, adapter: BaseAdapter, weight: float = 1.0):
        self.id = id
        self.adapter = adapter
        self.weight = weight

    async def query(self, request: QueryRequest) -> List[SearchResult]:
        start_time = time.perf_counter()
        try:
            results = await self.adapter.search(request)
            # Tag results with node origin and apply weight
            for res in results:
                res.node_id = self.id
                res.score *= self.weight
            return results
        except Exception as e:
            raise RuntimeError(f"Query failed on node {self.id}: {str(e)}")
