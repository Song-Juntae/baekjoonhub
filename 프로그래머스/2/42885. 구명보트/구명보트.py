from collections import deque

def solution(people, limit):
    if len(people) == 1:
        return 1
    sortp = deque(sorted(people))
    cnt = 0
    i = 0
    while len(sortp) > 1:
        if sortp.pop() + sortp[0] > limit:
            cnt += 1
        else:
            sortp.popleft()
            cnt += 1
    if len(sortp) > 0:
        cnt += 1
    return cnt