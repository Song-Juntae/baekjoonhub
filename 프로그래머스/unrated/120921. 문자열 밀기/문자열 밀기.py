from collections import deque

def solution(A, B):
    if A == B:
        return 0
    if len(A) == 1:
        return -1
    for i in range(1,len(A)+1):
        _ = deque(A)
        _.rotate(i)
        if _ == deque(B):
            return i
    return -1

# (b*2).find(a)