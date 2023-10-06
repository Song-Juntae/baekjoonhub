def solution(strArr):
    memo = {}
    for i in strArr:
        if len(i) not in memo:
            memo[len(i)] = 0
        memo[len(i)] += 1
    return max(memo.values())