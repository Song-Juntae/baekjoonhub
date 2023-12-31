from math import ceil, log2

def solution(n,a,b):
    max_ = max(a,b)
    min_ = min(a,b)
    cnt = 1
    while True:
        if max_ - min_ == 1:
            if max_ % 2 != 0:
                if min_ in [2**i for i in range(2,int(log2(n))+1)]:
                    cnt += log2(min_)
                else:
                    cnt += 1
            break
        else:
            max_ = ceil(max_/2)
            min_ = ceil(min_/2)
            cnt += 1
    return cnt

'''
def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer

def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()
'''