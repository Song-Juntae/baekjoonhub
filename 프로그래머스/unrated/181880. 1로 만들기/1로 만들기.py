import math

def solution(num_list):
    return sum([math.trunc(math.log(i,2)) for i in num_list])