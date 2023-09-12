import numpy as np

def solution(num_list):
    return int(np.prod(num_list) < sum(num_list)**2)