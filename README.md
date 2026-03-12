# VectorMesh

VectorMesh is a distributed query engine designed to execute semantic search queries across multiple, heterogeneous embedding databases (vector stores). It provides a unified interface to query fragmented data silos and aggregate results using configurable merging strategies.

## Key Features

*   **Federated Search**: Query multiple vector databases (Pinecone, Milvus, Qdrant, etc.) in parallel.
*   **Provider Agnostic**: Pluggable adapter system for different vector store backends.
*   **Smart Aggregation**: Merge results using RRF (Reciprocal Rank Fusion) or score-based normalization.
*   **Async First**: Built on Python's asyncio for high-concurrency network I/O.
*   **Type Safe**: Fully typed using Pydantic for request/response validation.

## Architecture

VectorMesh acts as a middleware layer:

1.  **Client** sends a query vector and metadata filters to the Mesh Engine.
2.  **Engine** identifies relevant "Nodes" (database instances) based on the query context.
3.  **Adapters** translate the generic query into provider-specific API calls.
4.  **Aggregator** collects results, normalizes scores, and applies ranking logic.
5.  **Response** is returned as a unified list of ranked documents.

## Installation

```bash
pip install vector-mesh
```

## Quick Start

```python
import asyncio
from vectormesh import MeshEngine, VectorNode
from vectormesh.adapters import MockAdapter

async def main():
    # Initialize nodes
    node_a = VectorNode(
        id="region-us-east",
        adapter=MockAdapter(name="Store A"),
        weight=1.0
    )
    node_b = VectorNode(
        id="region-eu-west",
        adapter=MockAdapter(name="Store B"),
        weight=0.8
    )

    # Create engine
    engine = MeshEngine(nodes=[node_a, node_b])

    # Execute search
    query_vector = [0.1, 0.2, 0.3]
    results = await engine.search(query_vector, top_k=5)

    for res in results:
        print(f"[{res.node_id}] Score: {res.score:.4f} - {res.metadata}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Configuration

Nodes can be configured via YAML or environment variables. Each node requires an adapter type and connection credentials.

## Contributing

Please see CONTRIBUTING.md for guidelines on adding new adapters or improving aggregation algorithms.
