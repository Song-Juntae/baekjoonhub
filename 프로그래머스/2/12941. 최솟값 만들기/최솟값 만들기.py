'''from itertools import permutations
from math import prod

def solution(A,B):
    return min(sum(prod(i) for i in zip(a,B)) for a in permutations(A))'''

def solution(A,B):
    answer = 0
    for a,b in zip(sorted(A),sorted(B, reverse=True)):
        answer += a*b
    return answer