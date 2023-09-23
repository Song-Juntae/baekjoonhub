def solution(n):
    return [[1 if idx2 == idx1 else 0 for idx2, j in enumerate(range(n))] for idx1, i in enumerate(range(n))]