def solution(s):
    cnt = 0
    x = s[0]
    dic = {'x':0,'notx':0}
    for i in s:
        if dic['x'] == dic['notx'] and dic['x'] != 0:
            dic['x'] = 0
            dic['notx'] = 0
            x = i
            cnt += 1
        if i == x:
            dic['x'] += 1
        elif i != x:
            dic['notx'] += 1
    return cnt+1
        
            