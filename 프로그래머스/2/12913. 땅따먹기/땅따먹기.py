def solution(land):
    memo = land.copy()
    for i in range(1,len(land)):
        memo[i][0] += max(land[i-1][1],land[i-1][2],land[i-1][3])
        memo[i][1] += max(land[i-1][0],land[i-1][2],land[i-1][3])
        memo[i][2] += max(land[i-1][0],land[i-1][1],land[i-1][3])
        memo[i][3] += max(land[i-1][0],land[i-1][1],land[i-1][2])
    return max(memo[-1])