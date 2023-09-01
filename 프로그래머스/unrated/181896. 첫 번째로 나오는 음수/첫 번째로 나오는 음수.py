def solution(num_list):
    list = [1 if i < 0 else 0 for i in num_list]
    if sum(list) == 0 : return -1
    return list.index(1)