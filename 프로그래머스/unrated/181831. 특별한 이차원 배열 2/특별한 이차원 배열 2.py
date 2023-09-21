from itertools import product

def solution(arr):
    len1 = len(arr)
    len2 = len(arr[0])
    for i in product(range(len1),range(len2)):
        if arr[i[0]][i[1]] == arr[i[1]][i[0]] : 
            continue
        else : 
            return 0
    return 1