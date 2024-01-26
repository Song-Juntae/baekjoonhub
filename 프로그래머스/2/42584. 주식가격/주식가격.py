from collections import deque

def solution(prices):
    d_prices = deque(prices)
    answer = []
    while d_prices:
        dp = d_prices.popleft()
        c = 0
        for p in d_prices:
            if dp > p:
                c += 1
                break
            else:
                c += 1
        answer.append(c)
    return answer