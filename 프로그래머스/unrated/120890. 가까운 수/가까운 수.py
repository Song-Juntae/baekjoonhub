def solution(array, n):
    _ = sorted(array, key = lambda x:(abs(x-n),x))
    return _[0]