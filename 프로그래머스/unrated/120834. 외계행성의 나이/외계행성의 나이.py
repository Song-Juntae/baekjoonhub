import string

def solution(age):
    dic = {f'{idx}':a for idx,a in enumerate(string.ascii_lowercase)}
    return "".join(dic[i] for i in f'{age}')