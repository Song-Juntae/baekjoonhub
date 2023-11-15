def solution(cards1, cards2, goal):
    _1 = [goal.index(i) if i in goal else len(goal)+1 for i in cards1]
    _2 = [goal.index(i) if i in goal else len(goal)+1 for i in cards2]
    if sorted(_1) == _1 and sorted(_2) == _2:
        return 'Yes'
    return 'No'