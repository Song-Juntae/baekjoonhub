from collections import Counter

def solution(topping):
    counter_topping = Counter(topping)
    dict_ = dict()
    lenc = len(counter_topping)
    len_ = 0
    cnt = 0
    for t in topping:
        if t not in dict_:
            dict_[t] = 1
            len_ += 1
        else:
            dict_[t] += 1
        if counter_topping[t] == 1:
            del counter_topping[t]
            lenc -= 1
        else:
            counter_topping[t] -= 1
        if lenc == len_:
            cnt += 1
    return cnt
            