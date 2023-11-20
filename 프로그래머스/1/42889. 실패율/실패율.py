from collections import Counter

def solution(N, stages):
    dic = Counter(stages)
    answer = dict()
    _ = len(stages)
    for i in range(1, N+1):
        if i not in dic:
            answer[i] = 0
        else:
            answer[i] = dic[i]/_
            _ -= dic[i]
    return sorted(answer, key=lambda x: answer[x], reverse=True)