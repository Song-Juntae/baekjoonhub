def f(n):
    memo=[1, 1]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        for i in range(2, n):
            memo.append(memo[-1]+memo[-2])
        return memo[-1]

def solution(n):
    return f(n) % 1234567