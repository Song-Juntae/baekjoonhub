def solution(k, m, score):
    _ = sorted(score, reverse=True)
    return sum(_[i]*m for i in range(m-1,len(score),m))