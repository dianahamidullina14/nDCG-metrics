from typing import List
import numpy as np


def cumulative_gain(relevance: List[float], k: int) -> float:
    score = 0
    for i in range(k):
        score += relevance[i]
    return score