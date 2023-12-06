def solution(s):
    cnt = 0
    cnt0 = 0
    while s != '1':
        cnt += 1
        cnt0 += s.count('0')
        s = s.replace('0','')
        s = f"{bin(len(s))}"[2:]
    return [cnt, cnt0]