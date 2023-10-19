from collections import deque

def solution(numbers, k):
    _ = deque(numbers)
    _.rotate(-2*(k-1))
    return _[0]