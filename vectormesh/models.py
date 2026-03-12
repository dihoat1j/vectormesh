from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class SearchResult(BaseModel):
    id: str
    score: float
    metadata: Dict[str, Any] = Field(default_factory=dict)
    node_id: Optional[str] = None
    vector: Optional[List[float]] = None

class QueryRequest(BaseModel):
    vector: List[float]
    top_k: int = 10
    filters: Dict[str, Any] = Field(default_factory=dict)
    include_metadata: bool = True
    include_vectors: bool = False

class NodeStatus(BaseModel):
    node_id: str
    is_active: bool
    latency_ms: float
    error: Optional[str] = None
