import numpy as np

def solution(arr1, arr2):
    _ = np.array(arr1)@np.array(arr2)
    return [[int(j) for j in i] for i in _]