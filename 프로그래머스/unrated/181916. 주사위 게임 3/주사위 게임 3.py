from collections import Counter

def solution(a, b, c, d):
    dict_ = dict(Counter([a,b,c,d]).items())
    if 4 in dict_.values():
        return 1111*a
    elif 3 in dict_.values():
        p = [i for i in dict_.items() if i[1] == 3][0][0]
        q = [i for i in dict_.items() if i[1] == 1][0][0]
        return (10 * p + q)**2
    elif 2 in dict_.values() and 1 not in dict_.values():
        p = list(dict_.keys())[0]
        q = list(dict_.keys())[1]
        return (p + q) * abs(p - q)
    elif 2 in dict_.values() and 1 in dict_.values():
        _ = [i[0] for i in dict_.items() if i[1] == 1]
        p = _[0]
        q = _[1]
        return p*q
    elif len(dict_) == 4:
        return min(a,b,c,d)
        