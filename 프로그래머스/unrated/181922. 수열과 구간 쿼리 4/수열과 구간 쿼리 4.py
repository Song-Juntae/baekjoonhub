def solution(arr, queries):
    memo = [0] * len(arr)
    for j in queries:
        for k in range(j[0],j[1]+1):
            if k % j[2] == 0:
                memo[k] += 1
    return [i+j for i, j in zip(arr,memo)]