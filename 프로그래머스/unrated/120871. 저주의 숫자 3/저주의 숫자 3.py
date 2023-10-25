def solution(n):
    cnt = 0
    for i in range(1,3*n+1):
        if cnt == n:
            return i - 1
        if '3' not in str(i) and i % 3:
            cnt += 1