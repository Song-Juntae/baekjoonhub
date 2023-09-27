def solution(numLog):
    dic = {
        1: 'w',
        -1: 's',
        10: 'd',
        -10: 'a'
    }
    return "".join([dic[numLog[idx+1] - i] if idx < len(numLog)-1 else "" for idx, i in enumerate(numLog)])