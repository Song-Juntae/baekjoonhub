import heapq

def solution(jobs):
    jobs.sort()
    a, t, i, s = 0, 0, 0, -1
    heap = []
    while i < len(jobs):
        for j in jobs:
            if s < j[0] <= t:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            p = heapq.heappop(heap)
            s = t
            t = t + p[0]
            a += t - p[1]
            i += 1
        else:
            t += 1
    return int(a/len(jobs))
