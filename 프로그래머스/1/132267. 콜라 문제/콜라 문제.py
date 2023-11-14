def solution(a, b, n):
    _ = n
    cnt = 0
    while _ >= a:
        cnt += _ // a * b
        _ = (_ // a * b) + (_ % a)
    return cnt