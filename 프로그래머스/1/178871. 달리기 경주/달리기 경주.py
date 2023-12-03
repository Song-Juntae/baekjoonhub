def solution(players, callings):
    dic_idx = {i:idx for idx,i in enumerate(players)}
    dic_i = {idx:i for idx,i in enumerate(players)}
    for i in callings:
        idx = dic_idx[i]
        h = dic_i[idx-1]
        dic_idx[i] -= 1
        dic_idx[h] += 1
        dic_i[idx] = h
        dic_i[idx-1] = i
    return sorted(dic_idx, key=lambda x:dic_idx[x])