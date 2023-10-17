def solution(array, height):
    memo = 0
    for i in array:
        if i > height:
            memo += 1
    return memo