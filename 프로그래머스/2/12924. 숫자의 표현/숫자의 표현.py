def solution(n):
    cnt = set([1, n])
    if n == 1:
        return 1
    if n % 2 != 0:
        cnt.update([n])
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            cnt.update([i, n/i])
    return len([i for i in cnt if i % 2 != 0])