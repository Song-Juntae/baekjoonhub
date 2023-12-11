memo = {0:1, 1:1}
memo = [1, 1]

def solution(n):
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(n-1):
            memo.append(memo[-2]+memo[-1])
    return memo[n] % 1234567