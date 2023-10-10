def solution(ineq, eq, n, m):
    if '!' not in eq:
        if eval(f'n {ineq}{eq} m'):
            return 1
        else:
            return 0
    else:
        if eval(f'n {ineq} m'):
            return 1
        else:
            return 0