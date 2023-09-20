def solution(arr, delete_list):
    tmp = set(arr) - set(delete_list)
    return [i for i in arr if i in tmp]