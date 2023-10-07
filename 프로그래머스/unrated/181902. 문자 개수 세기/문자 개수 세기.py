import string

def solution(my_string):
    return [my_string.count(i) for i in "".join([string.ascii_uppercase,string.ascii_lowercase])]