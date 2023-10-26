from collections import Counter
from math import prod

def solution(clothes):
    _ = Counter(i[1] for i in clothes).values()
    return prod(i + 1 for i in _) - 1