import asyncio
import logging
from typing import List
from vectormesh.models import QueryRequest, SearchResult
from vectormesh.node import VectorNode
from vectormesh.aggregation import RankFusion

logger = logging.getLogger(__name__)

class MeshEngine:
    def __init__(self, nodes: List[VectorNode], strategy: str = "score_merge"):
        self.nodes = nodes
        self.strategy = strategy
        self.aggregator = RankFusion()

    async def search(
        self, 
        vector: List[float], 
        top_k: int = 10, 
        filters: dict = None
    ) -> List[SearchResult]:
        request = QueryRequest(
            vector=vector, 
            top_k=top_k, 
            filters=filters or {}
        )
        
        # Execute parallel queries
        tasks = [node.query(request) for node in self.nodes]
        node_results = await asyncio.gather(*tasks, return_exceptions=True)
        
        flattened_results = []
        for i, result in enumerate(node_results):
            if isinstance(result, Exception):
                logger.error(f"Node {self.nodes[i].id} failed: {result}")
                continue
            flattened_results.append(result)
            
        # Aggregate and rank
        return self.aggregator.merge(flattened_results, limit=top_k)
