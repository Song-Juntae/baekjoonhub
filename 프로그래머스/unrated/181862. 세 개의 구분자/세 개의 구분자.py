def solution(myStr):
    if len([i for i in myStr.replace('a',' ').replace('b',' ').replace('c',' ').split(' ') if i != '']) == 0:
        return ['EMPTY']
    return [i for i in myStr.replace('a',' ').replace('b',' ').replace('c',' ').split(' ') if i != '']