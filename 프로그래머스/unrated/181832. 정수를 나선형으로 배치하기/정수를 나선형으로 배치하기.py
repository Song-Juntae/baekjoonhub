def solution(n):
    seq = [n//2 for n in range(1,2*n+1)][1::][::-1]
    seq = [seq[i * 4:(i + 1) * 4] for i in range((len(seq) + 4 - 1) // 4 )]
    seq[0][0] = seq[0][0] - 1
    number = [i for i in range(1,n**2+1)]
    x = 0
    y = 0
    idx_list = [[0,0]]
    answer = [[0]*n for i in range(n)]
    for i in seq:
        try:
            for j in range(i[0]):
                y = y + 1
                idx_list.append([x,y])
        except:
            pass
        try:
            for j in range(i[1]):
                x = x + 1
                idx_list.append([x,y])
        except:
            pass
        try:
            for j in range(i[2]):
                y = y - 1
                idx_list.append([x,y])
        except:
            pass
        try:
            for j in range(i[3]):
                x = x - 1
                idx_list.append([x,y])
        except:
            pass
    for i,j in zip(idx_list,number):
        answer[i[0]][i[1]] = j
    return answer
    
    