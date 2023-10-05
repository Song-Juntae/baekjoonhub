def solution(arr):
    if 2**(len(arr).bit_length() - 1) == len(arr) :
        return arr
    arr = arr + [0 for i in range(2**len(arr).bit_length()-len(arr))]
    return arr