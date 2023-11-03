def solution(a, b):
    _ = sorted([a, b])
    return sum(i for i in range(_[0],_[1]+1))