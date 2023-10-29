from collections import deque

def solution(priorities, location):
    sorted_priorities = sorted(priorities)
    queue = deque(i for i in enumerate(priorities))
    cnt = 0
    for i in range(10000):
        if sorted_priorities[-1] == queue[0][1]:
            sorted_priorities.pop(-1)
            cnt += 1
            if [queue[0][0], queue[0][1]] == [location,priorities[location]]:
                return cnt
            queue.popleft()
        else:
            queue.rotate(-1)