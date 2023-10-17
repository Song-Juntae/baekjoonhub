def solution(num_list):
    e, o = 0, 0
    for i in num_list:
        if i % 2 == 0:
            e += 1
        else:
            o += 1
    return [e,o]