import logging

def setup_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def normalize_score(score: float, min_val: float, max_val: float) -> float:
    if max_val == min_val:
        return 1.0
    return (score - min_val) / (max_val - min_val)
