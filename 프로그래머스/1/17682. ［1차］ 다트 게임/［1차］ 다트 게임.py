import re

def solution(dartResult):
    sets = re.findall(r'[0-9]*[SDT][#*]*',dartResult)
    total = []
    for i in sets:
        score = 0
        if 'S' in i:
            score += int(i[:i.index('S')])**1
        elif 'D' in i:
            score += int(i[:i.index('D')])**2
        elif 'T' in i:
            score += int(i[:i.index('T')])**3
        if '*' in i:
            if len(total) > 0:
                total[-1] = total[-1]*2
            total.append(score*2)
        elif '#' in i:
            total.append(-score)
        else:
            total.append(score)
    return sum(total)