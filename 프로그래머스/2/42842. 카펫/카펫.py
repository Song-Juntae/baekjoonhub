def solution(brown, yellow):
    _ = brown+yellow
    for i in range(int(_**0.5)+1, 2, -1):
        if _ % i == 0:
            max_ = max(_/i, i)
            min_ = min(_/i, i)
            if yellow == (max_-2)*(min_-2):
                return [max_, min_]