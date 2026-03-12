# Contributing to VectorMesh

Thank you for your interest in VectorMesh!

## Development Setup

1. Clone the repository
2. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Adding a New Adapter

To add support for a new vector database:
1. Create a new file in `vectormesh/adapters/`.
2. Inherit from `BaseAdapter`.
3. Implement `search` and `health_check`.
4. Add unit tests in `tests/`.

## Code Style

We use `black` for formatting and `isort` for import sorting. Please run these before submitting a PR.
