def solution(s):
    brackets = ['()', '{}', '[]']
    _ = s
    cnt = 0
    for i in range(len(_)):
        while any(x in _ for x in brackets):
            for br in brackets:
                _ = _.replace(br, '')
        if not _:
            cnt += 1
        s = s[1:]+s[0]
        _ = s
    return cnt