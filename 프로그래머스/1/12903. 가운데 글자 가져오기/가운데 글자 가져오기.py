def solution(s):
    _ = len(s)
    if _ == 1:
        return s
    elif _ % 2 == 0:
        return s[_//2-1:_//2+1]
    else:
        return s[_//2]