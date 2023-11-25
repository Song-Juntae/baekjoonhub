def solution(n, lost, reserve):
    cnt = n
    l = set(lost) - set(reserve)
    r = set(reserve) - set(lost)
    for i in sorted(l):
        if i - 1 in r:
            r.remove(i - 1)
        elif i + 1 in r:
            r.remove(i + 1)
        else:
            cnt -= 1
    return cnt