def solution(board, k):
    answer = 0
    for i in range(k+1) :
        for j in range(k+1) :
            if i + j <= k:
                try :
                    answer += board[i][j]
                except :
                    pass
    return answer