from collections import Counter

def solution(want, number, discount):
    dic = {key:value for key, value in zip(want, number)}
    cnt = 0
    for i in range(1,len(discount)-8):
        if Counter(dic) - Counter(discount[-i:-10-i:-1]) == {}:
            cnt += 1
    return cnt