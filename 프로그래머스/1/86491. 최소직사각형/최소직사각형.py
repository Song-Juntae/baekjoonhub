def solution(sizes):
    width = 0
    length = 0
    for i,j in sizes:
        if max(i,j) >= width:
            width = max(i,j)
        if min(i,j) >= length:
            length = min(i,j)
    return width * length