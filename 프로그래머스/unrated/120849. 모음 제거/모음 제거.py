def solution(my_string):
    dic = {'a':'', 'e':'', 'i':'', 'o':'', 'u':''}
    return my_string.translate(str.maketrans(dic))