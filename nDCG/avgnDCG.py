from typing import List
import numpy as np


def avg_ndcg(list_relevances: List[List[float]], k: int, method: str = 'standard') -> float:

    if method not in ['standard', 'industry']:
        raise ValueError

    result = 0.0

    if len(list_relevances) == 0:
        return 0.0

    for j in list_relevances:
        dcg = 0.0
        idcg = 0.0

        for i in range(k):
            if i < len(j):  # Проверяем, есть ли элемент на i-й позиции
                if method == 'standard':
                    dcg += (j[i] / np.log2(i + 2))
                elif method == 'industry':
                    dcg += ((pow(2, j[i]) - 1) / np.log2(i + 2))

        sorted_relevance = sorted(j, reverse=True)
        for i in range(k):
            if i < len(sorted_relevance):  # Проверяем, есть ли элемент на i-й позиции
                if method == 'standard':
                    idcg += (sorted_relevance[i] / np.log2(i + 2))
                elif method == 'industry':
                    idcg += ((pow(2, sorted_relevance[i]) - 1) / np.log2(i + 2))

        if idcg > 0:
            result += dcg / idcg

    score = result / len(list_relevances)

    return score