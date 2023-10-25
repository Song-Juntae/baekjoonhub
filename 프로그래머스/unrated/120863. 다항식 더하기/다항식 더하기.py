def solution(polynomial):
    if '+' not in polynomial:
        return polynomial
    x = 0
    s = 0
    for i in polynomial.split(' + '):
        if 'x' in i:
            if len(i) > 1:
                x += int(i[:-1])
            else:
                x += 1
        else:
            s += int(i)
    if x == 0:
        return f'{s}'
    elif s == 0:
        if x == 1:
            return f'x'
        else:
            return f'{x}x'
    else:
        if x == 1:
            return f'x + {s}'
        else:
            return f'{x}x + {s}'
            