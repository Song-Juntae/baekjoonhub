def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for b in babbling:
        _ = b
        match = ''
        while True:
            if _ == '':
                cnt += 1
                break
            elif _[:3] in words and _[:3] != match:
                match = _[:3]
                _ = _[3:]
            elif _[:2] in words and _[:2] != match:
                match = _[:2]
                _ = _[2:]
            else:
                break
    return cnt