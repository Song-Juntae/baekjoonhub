def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        _ = s[i]
        if _ not in dic:
            answer.append(-1)
            dic[_] = i
        else:
            answer.append(i - dic[_])
            dic[_] = i
    return answer