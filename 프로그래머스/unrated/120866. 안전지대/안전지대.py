def solution(board):
    mine = []
    for idx_i, i in enumerate(board):
        for idx_j, j in enumerate(i):
            if j == 1:
                mine.append((idx_i,idx_j))
    limit = len(board)
    total = limit * limit
    danger = []
    for i in mine:
        danger += [(i[0] - 1, i[1] + 1), (i[0], i[1] + 1), (i[0] + 1, i[1] + 1), 
                   (i[0] - 1, i[1]), (i[0], i[1]), (i[0] + 1, i[1]),
                   (i[0] - 1, i[1] - 1), (i[0], i[1] - 1), (i[0] + 1, i[1] - 1)]
    danger = [i for i in danger if 0 <= i[0] < limit and 0 <= i[1] < limit]
    return total - len(set(danger))