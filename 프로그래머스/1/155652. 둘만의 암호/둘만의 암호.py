from string import ascii_lowercase

def solution(s, skip, index):
    _ = ascii_lowercase * len(s)
    for i in skip:
        _ = _.replace(i,'')
    return ''.join(_[_.find(i)+index] for i in s)