def solution(arr):
    stk = []
    _ = 0
    while True:
        try:
            if len(stk) == 0:
                stk.append(arr[_])
                _ += 1
            else:
                if stk[-1] < arr[_]:
                    stk.append(arr[_])
                    _ += 1
                else:
                    del stk[-1]
        except:
            return stk