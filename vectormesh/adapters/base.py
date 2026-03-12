from abc import ABC, abstractmethod
from typing import List
from vectormesh.models import QueryRequest, SearchResult

class BaseAdapter(ABC):
    @abstractmethod
    async def search(self, request: QueryRequest) -> List[SearchResult]:
        """Execute search against the specific vector database."""
        pass

    @abstractmethod
    async def health_check(self) -> bool:
        """Check if the database is reachable."""
        pass
