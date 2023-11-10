def solution(n):
    _ = n
    answer = ''
    while _:
        answer += str(_ % 3)
        _ = _ // 3
    return int(answer, 3)