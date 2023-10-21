def solution(n):
    _ = n
    for i in range(1,n+2):
        if _ / i >= 1:
            _ = _ / i
        elif _ / i < 1:
            return i - 1