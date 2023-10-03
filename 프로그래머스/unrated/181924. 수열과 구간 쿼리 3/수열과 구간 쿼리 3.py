def solution(arr, queries):
    for i in queries:
        i0 = arr[i[0]]
        i1 = arr[i[1]]
        arr[i[0]] = i1
        arr[i[1]] = i0
    return arr