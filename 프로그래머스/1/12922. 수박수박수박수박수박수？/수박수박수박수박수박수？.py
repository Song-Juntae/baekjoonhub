def solution(n):
    _ = '수박'
    index = 0
    answer = ''
    for i in range(n):
        if index == 0:
            answer += _[index]
            index = 1
        elif index == 1:
            answer += _[index]
            index = 0
    return answer