def solution(n):
    if n == 1:
        return 1
    if (n ** 0.5).is_integer():
        return 1
    return 2