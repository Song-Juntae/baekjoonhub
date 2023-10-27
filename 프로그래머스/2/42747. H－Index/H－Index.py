def solution(citations):
    _ = sorted(citations, reverse=True)
    if _[0] == 0:
        return 0
    elif _[0] == 1:
        return 1
    for idx, i in enumerate(_):
        if i < idx+1:
            return idx
    return idx + 1