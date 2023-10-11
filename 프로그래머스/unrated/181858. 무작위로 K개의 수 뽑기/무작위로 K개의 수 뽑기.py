def solution(arr, k):
    memo = []
    for i in arr:
        if i not in memo:
            memo.append(i)
        if len(memo) == k:
            break
    if len(memo) < k:
        memo += [-1]*(k-len(memo))
    return memo[:k]