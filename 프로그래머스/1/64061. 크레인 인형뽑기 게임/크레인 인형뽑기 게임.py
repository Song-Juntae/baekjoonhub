def solution(board, moves):
    board_stack = [[j for j in i if j != 0] for i in zip(*board)]
    s = []
    cnt = 0
    for m in moves:
        if len(board_stack[m-1]) > 0:
            s.append(board_stack[m-1].pop(0))
        if len(s) > 1:
            if s[-1] == s[-2]:
                s.pop(-1)
                s.pop(-1)
                cnt += 2
    return cnt