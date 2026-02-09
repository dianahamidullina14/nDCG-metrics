from typing import List

import numpy as np


def discounted_cumulative_gain(relevance: List[float], k: int, method: str = "standard") -> float:
    score = 0
    for i in range(k):
        if method == 'standard':
            score += (relevance[i]/np.log2(i + 2))
        elif method == 'industry':
            score += ((pow(2,relevance[i]) - 1)/ np.log2(i + 2))
        else:
            raise ValueError

    return score