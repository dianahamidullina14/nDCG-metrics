from typing import List
import numpy as np


def normalized_dcg(relevance: List[float], k: int, method: str = "standard") -> float:
    dcg = 0.0
    idcg = 0.0
    for i in range(k):
        if method == 'standard':
            dcg += (relevance[i]/np.log2(i + 2))
        elif method == 'industry':
            dcg += ((pow(2,relevance[i]) - 1)/ np.log2(i + 2))
        else:
            raise ValueError


    sorted_relevance = sorted(relevance, reverse=True)
    for i in range(k):
        if method == 'standard':
            idcg += (sorted_relevance[i]/np.log2(i + 2))
        elif method == 'industry':
            idcg += ((pow(2,sorted_relevance[i]) - 1)/ np.log2(i + 2))
        else:
            raise ValueError

    score = dcg/idcg
    return score