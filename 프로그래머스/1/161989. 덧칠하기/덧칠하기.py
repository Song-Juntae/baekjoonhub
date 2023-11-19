def solution(n, m, section):
    cnt = 1
    sec = section[0] + m - 1
    for i in section:
        if i > sec:
            cnt += 1
            sec = i + m - 1
    return cnt