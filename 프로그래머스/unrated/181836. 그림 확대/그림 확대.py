def solution(picture, k):
    memo = []
    for i in picture:
        memo += [''.join([j*k for j in i])]*k
    return memo