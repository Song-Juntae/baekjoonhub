from collections import Counter

def solution(array):
    if [i for i in Counter(array).values()].count(max(Counter(array).values())) > 1:
        return -1
    return sorted(Counter(array).items(), key=lambda x: x[1])[-1][0]