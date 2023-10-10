def solution(arr):
    if len(arr) == len(arr[0]):
        return arr
    elif len(arr) > len(arr[0]):
        return [i + [0]*(len(arr) - len(arr[0])) for i in arr]
    elif len(arr) < len(arr[0]):
        return arr + (len(arr[0])-len(arr))*[[0]*len(arr[0])]