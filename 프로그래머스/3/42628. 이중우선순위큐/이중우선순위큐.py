import heapq

def solution(operations):
    heap = []
    for o in operations:
        if o[0] == 'I':
            heapq.heappush(heap,int(o[2:]))
        elif len(heap) > 0:
            if o[-2:] == '-1':
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))
    if len(heap) > 0:
        return [max(heap), heapq.heappop(heap)]
    else:
        return [0,0]