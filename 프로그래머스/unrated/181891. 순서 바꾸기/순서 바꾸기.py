from collections import deque

def solution(num_list, n):
    answer = deque(num_list)
    answer.rotate(-n)
    return list(answer)