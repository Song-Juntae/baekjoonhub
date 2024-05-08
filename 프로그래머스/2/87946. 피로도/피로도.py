from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for p in permutations(dungeons, len(dungeons)):
        cnt = 0
        k_copy = k
        for d in p:
            if k_copy >= d[0]:
                k_copy = k_copy - d[1]
                cnt += 1
        if cnt > answer:
            answer = cnt
    return answer