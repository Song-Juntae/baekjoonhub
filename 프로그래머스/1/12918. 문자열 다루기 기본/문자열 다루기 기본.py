def solution(s):
    lens = len(s)
    if lens == 4 or lens == 6:
        for i in s:
            if i.isdigit() == False:
                return False
        return True
    return False