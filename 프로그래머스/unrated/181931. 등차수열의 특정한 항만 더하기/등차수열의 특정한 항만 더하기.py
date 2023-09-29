from itertools import compress

def solution(a, d, included):
    return sum(compress(range(a,(a+(len(included)+1)*d),d),included))