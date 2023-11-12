from string import ascii_lowercase as al, ascii_uppercase as au
 
def solution(s, n):
    _ = al+al+au+au
    return ''.join([_[_.find(i)+n] if _.find(i) != -1 else ' ' for i in s])