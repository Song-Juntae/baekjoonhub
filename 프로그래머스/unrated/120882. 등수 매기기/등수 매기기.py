def solution(score):
    _ = [-(sum(i)/2) for i in score]
    s = sorted([-(sum(i)/2) for i in score])
    return [s.index(i)+1 for i in _]