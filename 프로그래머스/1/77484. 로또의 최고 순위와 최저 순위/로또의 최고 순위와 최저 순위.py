def solution(lottos, win_nums):
    _ = len(set(win_nums) & set(lottos))
    n_0 = lottos.count(0)
    max_ = _ + n_0
    min_ = _ 
    return [6,6,5,4,3,2,1][max_],[6,6,5,4,3,2,1][min_]