def solution(myString, pat):
    return int(pat.lower().replace('a','B').replace('b','A') in myString)