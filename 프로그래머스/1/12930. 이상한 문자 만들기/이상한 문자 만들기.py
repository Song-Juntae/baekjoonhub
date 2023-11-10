def solution(s):
    s = s.lower()
    return ' '.join(''.join(k[i].upper() if (i+2) % 2 == 0 else k[i] for i in range(len(k))) for k in s.split(' '))