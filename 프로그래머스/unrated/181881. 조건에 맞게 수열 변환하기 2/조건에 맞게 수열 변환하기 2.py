def func(n):
    if n >= 50 and n % 2 == 0:
        n = n / 2
    elif n < 50 and n % 2 != 0:
        n = (n * 2) + 1
    else:
        pass
    return n

def solution(arr):
    counts = {}
    if arr == [func(i) for i in arr]:
        return 0
    for idx,i in enumerate(arr):
        pre = i
        if idx not in counts:
            counts[idx] = 0
        while pre != func(pre):
            counts[idx] += 1
            pre = func(pre)
    return max(counts.values())
            
    