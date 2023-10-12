def solution(rank, attendance):
    memo = dict()
    for idx, i in enumerate(attendance):
        if i :
            memo[rank[idx]] = idx
    memo = sorted(memo.items())
    return memo[0][1]*10000+memo[1][1]*100+memo[2][1]