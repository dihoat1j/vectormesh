from typing import List
from vectormesh.models import SearchResult

def reciprocal_rank_fusion(
    results_list: List[List[SearchResult]], 
    k: int = 60
) -> List[SearchResult]:
    """
    Standard RRF algorithm for merging ranked lists.
    """
    scores: dict = {}
    doc_map: dict = {}
    
    for results in results_list:
        for rank, res in enumerate(results):
            if res.id not in scores:
                scores[res.id] = 0.0
                doc_map[res.id] = res
            scores[res.id] += 1.0 / (k + rank + 1)
            
    # Sort by RRF score
    sorted_ids = sorted(scores.keys(), key=lambda x: scores[x], reverse=True)
    
    final_results = []
    for doc_id in sorted_ids:
        doc = doc_map[doc_id]
        # Update score to RRF score
        doc.score = scores[doc_id]
        final_results.append(doc)
        
    return final_results
