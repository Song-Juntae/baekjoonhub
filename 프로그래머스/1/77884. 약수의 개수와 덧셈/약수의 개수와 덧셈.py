def divisor_count(n):
    _ = {1,n}
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            _.update([i, n/i])
    return len(_)

def solution(left, right):
    return sum(i if divisor_count(i) % 2 == 0 else -i for i in range(left, right+1))