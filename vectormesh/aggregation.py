from typing import List, Dict
from vectormesh.models import SearchResult

class RankFusion:
    @staticmethod
    def merge(
        node_results: List[List[SearchResult]], 
        limit: int = 10
    ) -> List[SearchResult]:
        """
        Simple score-based merging. 
        In production, this would implement RRF or Borda count.
        """
        all_results = []
        for results in node_results:
            all_results.extend(results)
            
        # Sort by score descending
        sorted_results = sorted(
            all_results, 
            key=lambda x: x.score, 
            reverse=True
        )
        
        # Deduplicate by ID if necessary
        seen_ids = set()
        unique_results = []
        for res in sorted_results:
            if res.id not in seen_ids:
                unique_results.append(res)
                seen_ids.add(res.id)
                
        return unique_results[:limit]
