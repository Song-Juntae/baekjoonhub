def solution(k, score):
    _ = []
    answer = []
    for i in score:
        _.append(i)
        try:
            _ = sorted(_, reverse=True)[:k]
        except:
            pass
        answer.append(_[-1])
    return answer