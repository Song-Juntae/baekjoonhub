def solution(n, m, section):
    _sum = 0
    cnt = 1
    for i,j in zip(section[:-1], section[1:]):
        _ = j - i
        if _ <= m:
            _sum += _
        elif _ > m:
            cnt += 1
            _ = 0
        if _sum >= m:
            cnt += 1
            _sum = 0
    return cnt