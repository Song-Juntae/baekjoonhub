def solution(spell, dic):
    for i in dic:
        _ = 0
        for j in spell:
            if i.count(j) == 1:
                _ += 1
        if _ == len(spell):
            return 1
    return 2
    