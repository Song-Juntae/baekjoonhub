from math import ceil

def solution(progresses, speeds):
    answer = [1]
    memo = ceil((100 - progresses[0])/speeds[0])
    for i in range(1,len(progresses)):
        if memo >= ceil((100 - progresses[i])/speeds[i]):
            answer[-1] += 1
        else:
            memo = ceil((100 - progresses[i])/speeds[i])
            answer.append(1)
    return answer