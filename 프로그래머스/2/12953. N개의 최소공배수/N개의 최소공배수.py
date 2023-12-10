from math import prod

def solution(arr):
    maxarr = max(arr)
    for i in range(1,prod(arr)):
        h = maxarr*i
        if all(h%a == 0 for a in arr):
            return h
            