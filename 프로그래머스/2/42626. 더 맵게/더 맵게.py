import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        _ = heapq.heappop(scoville)
        if _ < K:
            heapq.heappush(scoville, _+heapq.heappop(scoville)*2)
            cnt += 1
        else:
            return cnt
    if scoville[0] >= K:
        return cnt
    return -1