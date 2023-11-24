from collections import Counter

def solution(X, Y):
    cntX = Counter(X)
    cntY = Counter(Y)
    answer = ''.join(sorted([key*value for key,value in dict(cntX & cntY).items()], reverse=True))
    if answer == '':
        return '-1'
    elif answer.replace('0','') == '':
        return '0'
    else:
        return answer