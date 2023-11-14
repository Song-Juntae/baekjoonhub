def solution(name, yearning, photo):
    dic = dict(zip(name,yearning))
    return [sum([dic[j] for j in i if j in name]) for i in photo ]