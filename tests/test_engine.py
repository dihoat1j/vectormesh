import pytest
import asyncio
from vectormesh.engine import MeshEngine
from vectormesh.node import VectorNode
from vectormesh.adapters.mock import MockAdapter

@pytest.mark.asyncio
async def test_engine_search_aggregation():
    node1 = VectorNode("n1", MockAdapter("A"))
    node2 = VectorNode("n2", MockAdapter("B"))
    engine = MeshEngine(nodes=[node1, node2])
    
    results = await engine.search(vector=[0.1, 0.1], top_k=5)
    
    assert len(results) == 5
    assert results[0].score >= results[-1].score
    assert all(r.node_id in ["n1", "n2"] for r in results)

@pytest.mark.asyncio
async def test_engine_node_failure_handling():
    class FailingAdapter(MockAdapter):
        async def search(self, req):
            raise ValueError("Database connection lost")

    node1 = VectorNode("n1", MockAdapter("A"))
    node2 = VectorNode("fail", FailingAdapter("B"))
    engine = MeshEngine(nodes=[node1, node2])
    
    # Should not raise exception, just log and continue
    results = await engine.search(vector=[0.1], top_k=2)
    assert len(results) > 0
    assert all(r.node_id == "n1" for r in results)
