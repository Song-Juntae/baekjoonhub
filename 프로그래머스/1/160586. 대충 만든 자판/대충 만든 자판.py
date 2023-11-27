def solution(keymap, targets):
    setk = set(''.join(i for i in keymap))
    answer = []
    for t in targets:
        cnt = 0
        if set(t) - setk == set():
            for i in t:
                cnt += min([k.find(i) + 1 if k.find(i) != -1 else 101 for k in keymap])
            answer.append(cnt)
        else:
            answer.append(-1)
    return answer