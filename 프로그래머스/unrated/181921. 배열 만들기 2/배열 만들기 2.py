def solution(l, r):
    answer = []
    for i in range(64):
        if 5*int(bin(i)[2:]) >= l and 5*int(bin(i)[2:]) <= r:
            answer.append(5*int(bin(i)[2:]))
        elif 5*int(bin(i)[2:]) > r:
            break
    if answer == []:
        return [-1]
    return answer