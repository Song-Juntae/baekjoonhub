from itertools import combinations
import math

def isprime(n):
    for j in range(2, int(math.sqrt(n))+1):
        if n % j == 0:
            return False
    return True

def solution(nums):
    cnt = 0
    for i in combinations(nums,3):
        _ = sum(i)
        if isprime(_):
            cnt += 1
    return cnt