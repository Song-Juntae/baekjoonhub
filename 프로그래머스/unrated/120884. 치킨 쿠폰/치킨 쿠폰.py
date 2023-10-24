def solution(chicken):
    cnt = 0
    for i in range(1,7):
        cnt += chicken//10
        chicken = chicken//10 + chicken%10
    return cnt

    