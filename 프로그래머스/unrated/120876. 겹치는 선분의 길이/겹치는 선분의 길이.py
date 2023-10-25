def solution(lines):
    cnt = 0
    _ = [set(range(i[0],i[1] + 1)) for i in lines]
    if len(_[0] & _[1]) >= 2:
        cnt += len(_[0] & _[1]) -1
    if len(_[1] & _[2]) >= 2:
        cnt += len(_[1] & _[2]) -1
    if len(_[0] & _[2]) >= 2:
        cnt += len(_[0] & _[2]) -1
    if len(_[0] & _[1] & _[2]) >= 2:
        cnt -= 2*(len(_[0] & _[1] & _[2]) - 1)
    return cnt
        