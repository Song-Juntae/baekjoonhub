from fractions import Fraction

def solution(a, b):
    num, den = Fraction(a,b).numerator, Fraction(a,b).denominator
    f = []
    d = 2
    while den > 1:
        while den % d == 0:
            f.append(d)
            den //= d
        d += 1
    if len(set(f) - set([1,2,5])) == 0:
        return 1
    else:
        return 2