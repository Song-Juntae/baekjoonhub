def solution(n):
    cnt = 1
    while n / 2 > 1:
        if n % 2 != 0:
            n = n - 1
            cnt += 1
        n = n/2
    return cnt