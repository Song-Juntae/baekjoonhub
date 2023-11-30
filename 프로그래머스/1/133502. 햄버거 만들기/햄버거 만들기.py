def solution(ingredient):
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if len(s) >= 4:
            if s[-4:] == [1,2,3,1]:
                cnt += 1
                del s[-1]
                del s[-1]
                del s[-1]
                del s[-1]
    return cnt