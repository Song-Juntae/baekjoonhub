def solution(s):
    return sum(-int(s.split(' ')[idx-1]) if i == 'Z' else int(i) for idx, i in enumerate(s.split(' ')) )