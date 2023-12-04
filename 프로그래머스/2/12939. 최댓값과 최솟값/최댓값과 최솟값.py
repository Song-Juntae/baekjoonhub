def solution(s):
    _ = [int(i) for i in s.split(' ')]
    return f'{min(_)} {max(_)}'