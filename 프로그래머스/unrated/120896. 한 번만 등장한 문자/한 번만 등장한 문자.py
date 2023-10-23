from string import ascii_lowercase

def solution(s):
    return ''.join(i for i in ascii_lowercase if s.count(i) == 1)