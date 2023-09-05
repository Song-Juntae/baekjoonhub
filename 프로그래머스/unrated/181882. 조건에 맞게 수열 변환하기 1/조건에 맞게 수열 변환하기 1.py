def solution(arr):
    return [i/2 if (i >= 50) and (i % 2 == 0) else i if (i >= 50) or (i % 2 == 0) else i*2 for i in arr]