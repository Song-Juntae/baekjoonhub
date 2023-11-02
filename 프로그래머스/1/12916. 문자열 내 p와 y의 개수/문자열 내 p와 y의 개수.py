from collections import Counter

def solution(s):
    _ = Counter(s.lower())
    if _['p'] == _['y']:
        return True
    return False