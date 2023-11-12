def solution(s):
    return [s[:i][::-1].find(s[i])+1 if s[:i][::-1].find(s[i]) != -1 else s[:i][::-1].find(s[i])  for i in range(len(s))]