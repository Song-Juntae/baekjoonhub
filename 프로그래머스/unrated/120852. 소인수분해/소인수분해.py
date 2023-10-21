import math
 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(n):
    answer = []
    if is_prime(n):
        return [n]
    for i in range(2, n):
        if is_prime(i):
            if n % i == 0:
                answer.append(i)
    return answer