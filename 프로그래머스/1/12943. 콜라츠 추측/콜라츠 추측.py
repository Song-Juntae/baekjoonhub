def solution(num):
    if num == 1:
        return 0
    cnt = 0
    for i in range(500):
        if num == 1:
            return cnt
        elif num % 2 == 0:
            num = num / 2
            cnt += 1
        elif num % 2 != 0:
            num = num * 3 + 1
            cnt += 1
    return -1