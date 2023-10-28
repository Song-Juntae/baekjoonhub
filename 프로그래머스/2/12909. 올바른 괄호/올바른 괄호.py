# tmi Catalan number (a(b))c 가능한 조합의 수

def solution(s):
    memo = []
    if len(s) % 2 != 0:
        return False
    if s[0] == ')':
        return False
    for i in s:
        if i == '(':
            memo.append('(')
        if i == ')':
            try:
                memo.pop(-1)
            except:
                return False
    return memo == []