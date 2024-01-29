from itertools import permutations as pm

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    set_ = set()
    cnt = 0
    for i in range(1,len(numbers)+1):
        for p in pm(numbers, i):
            num = int(''.join(p))
            if num != 0 and num != 1:
                set_.add(num)
    for n in set_:
        if is_prime(n):
            cnt += 1
    return cnt