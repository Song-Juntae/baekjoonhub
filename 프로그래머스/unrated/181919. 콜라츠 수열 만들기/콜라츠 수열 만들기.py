def solution(n):
    answer = [n]
    while answer[-1] != 1:
        if answer[-1] % 2 == 0 :
            answer += [answer[-1] / 2]
        else :
            answer += [answer[-1] * 3 + 1]
    return answer