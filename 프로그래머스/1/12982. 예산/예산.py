def solution(d, budget):
    _ = sorted(d)
    answer = 0
    for i in range(len(_)):
        if sum(_[:i+1]) > budget:
            return i
    return len(_)