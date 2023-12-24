def solution(x, y, n):
    sety = set([y])
    cnt = 0
    while x not in sety:
        set_ = set()
        for i in sety:
            if i % 3 == 0:
                set_.add(i/3)
            if i % 2 == 0:
                set_.add(i/2)
            if i-n > 0:
                set_.add(i-n)
            if i%3 != 0 and i%2 != 0 and i-n < 0:
                return -1
        cnt += 1
        sety = sety and set_
    return cnt