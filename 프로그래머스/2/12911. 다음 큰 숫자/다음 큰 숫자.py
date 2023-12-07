def solution(n):
    _ = bin(n)
    if _ == '1':
        return 2
    elif _[-2:] == '01':
        return n+1
    elif _[-2:] == '010':
        return n+2
    elif _.count('0') == 0:
        return int(f'10{_[:-1]}',2)
    else:
        answer = n+1
        while bin(answer).count('1') != _.count('1'):
            answer += 1
        return answer