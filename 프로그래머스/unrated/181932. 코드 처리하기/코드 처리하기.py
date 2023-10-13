def solution(code):
    if code.replace('1','')[::2] == '':
        return 'EMPTY'
    return code.replace('1','')[::2]