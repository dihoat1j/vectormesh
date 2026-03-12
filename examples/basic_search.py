import asyncio
from vectormesh import MeshEngine, VectorNode
from vectormesh.adapters.mock import MockAdapter

async def run_example():
    # Setup nodes representing different data shards or regions
    nodes = [
        VectorNode("docs-v1", MockAdapter("LegacyDocs", latency_range=(0.1, 0.2))),
        VectorNode("docs-v2", MockAdapter("CurrentDocs", latency_range=(0.01, 0.05))),
        VectorNode("wiki", MockAdapter("ExternalWiki", latency_range=(0.2, 0.4)))
    ]

    engine = MeshEngine(nodes=nodes)

    print("Querying distributed mesh...")
    results = await engine.search(
        vector=[0.5] * 128, 
        top_k=3
    )

    for i, res in enumerate(results):
        print(f"{i+1}. [{res.node_id}] ID: {res.id} | Score: {res.score:.3f}")

if __name__ == "__main__":
    asyncio.run(run_example())
