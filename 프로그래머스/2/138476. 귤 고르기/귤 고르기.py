from collections import Counter

def solution(k, tangerine):
    cntt = Counter(tangerine)
    sortt = sorted(cntt.values(), reverse=True)
    cnt = 0
    _ = 0
    for i in sortt:
        if _ >= k:
            break
        _ += i
        cnt += 1
    return cnt