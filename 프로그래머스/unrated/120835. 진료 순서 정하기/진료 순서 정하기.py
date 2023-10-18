def solution(emergency):
    memo = sorted(emergency, reverse=True)
    return [memo.index(i)+1 for i in emergency]