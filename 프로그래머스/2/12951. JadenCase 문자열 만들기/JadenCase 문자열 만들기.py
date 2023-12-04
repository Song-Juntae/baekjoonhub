def solution(s):
    answer = ''
    first = True
    for i in s:
        if i == ' ':
            first = True
            answer += ' '
        elif first:
            first = False
            answer += i.upper()
        else:
            answer += i.lower()
    return answer