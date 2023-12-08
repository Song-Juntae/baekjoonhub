def solution(s):
    stk = [s[0]]
    for i in s[1:]:
        stk.append(i)
        while len(stk) > 1 and stk[-2] == stk[-1]:
            stk.pop(-1)
            stk.pop(-1)
    if len(stk) > 0:
        return 0
    else:
        return 1