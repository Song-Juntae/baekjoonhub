def solution(answers):
    _1 = [1, 2, 3, 4, 5]
    _2 = [2, 1, 2, 3, 2, 4, 2, 5]
    _3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    lena = len(answers)
    a1 = 0
    a2 = 0
    a3 = 0
    for idx, i in enumerate(answers):
        if i == _1[idx % 5]:
            a1 += 1
        if i == _2[idx % 8]:
            a2 += 1
        if i == _3[idx % 10]:
            a3 += 1
    return [idx+1 for idx,i in enumerate([a1,a2,a3]) if i == max(a1,a2,a3)]