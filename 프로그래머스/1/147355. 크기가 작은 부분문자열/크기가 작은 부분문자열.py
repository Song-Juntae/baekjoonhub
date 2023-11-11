def solution(t, p):
    lenp = len(p)
    lent = len(t)
    return len([t[i-lenp:i] for i in range(lenp,lent+1) if t[i-lenp:i] <= p])