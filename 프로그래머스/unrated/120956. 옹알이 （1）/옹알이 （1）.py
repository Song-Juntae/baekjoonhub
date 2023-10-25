from itertools import permutations

def solution(babbling):
    word = []
    for i in range(1,5):
        for j in permutations(["aya", "ye", "woo", "ma"], i):
            word.append(''.join(j))
    cnt = 0
    for i in babbling:
        if i in word:
            cnt += 1
    return cnt