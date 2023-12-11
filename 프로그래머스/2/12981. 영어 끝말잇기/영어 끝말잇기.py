from math import ceil 

def solution(n, words):
    setw = dict()
    when = 0
    word = ''
    for idx, i in enumerate(words):
        if len(i) < 2:
                when = idx + 1
                break
        elif i not in setw:
            setw[i] = True
            if idx != 0 and word[-1] != i[0]:
                when = idx + 1
                break
        else:
            when = idx + 1
            break
        word = i
    if when == 0:
        return [0,0]
    elif when % n == 0:
        who = n
        return [who, ceil(when / n)]
    else:
        who = range(n+1)[when % n]
        return [who, ceil(when / n)]