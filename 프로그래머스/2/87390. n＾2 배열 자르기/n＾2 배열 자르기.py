'''def solution(n, left, right):
    _ = [*[k for k in range(1,n+1)]]
    for i in range(2,n+1):
        _ += [i]*i
        _ += [k for k in range(1+i,n+1)]
    return _[left:right+1]'''

def solution(n, left, right):
    arr = []
    for i in range(left+1,right+2):
        _ = divmod(i,n)
        if _[1] == 0:
            arr.append(n)
        elif _[0] >= _[1]:
            arr.append(_[0]+1)
        else:
            arr.append(_[1])
    return arr