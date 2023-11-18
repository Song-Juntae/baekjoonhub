def n_divisor(n):
    d = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            d.update([i, n/i])
    return len(d)

def solution(number, limit, power):
    sum = 0
    for i in range(1, number+1):
        _ = n_divisor(i)
        if _ > limit:
            sum += power
        else:
            sum += _
    return sum