

def solution(keyinput, board):
    coord_x = 0
    coord_y = 0
    coord_x_plus = (board[0] - 1)/2
    coord_x_minus = -((board[0] - 1)/2)
    coord_y_plus = (board[1] - 1)/2
    coord_y_minus = -((board[1] - 1)/2)
    for i in keyinput:
        if i == 'left':
            if coord_x - 1 >= coord_x_minus:
                coord_x = coord_x - 1
        elif i == 'right':
            if coord_x + 1 <= coord_x_plus:
                coord_x = coord_x + 1
        elif i == 'up':
            if coord_y + 1 <= coord_y_plus:
                coord_y = coord_y + 1
        elif i == 'down':
            if coord_y - 1 >= coord_y_minus:
                coord_y = coord_y - 1
    return [coord_x, coord_y]