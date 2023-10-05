def solution(myString, pat):
    memo = 0
    start = 0
    end = len(pat)
    for i in range(len(myString)):
        if myString[start:end] == pat:
            memo += 1
        start += 1
        end += 1
    return memo