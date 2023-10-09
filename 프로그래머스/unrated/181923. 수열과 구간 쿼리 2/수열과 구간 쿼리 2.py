def solution(arr, queries):
    answer = []
    for (s,e,k) in queries:
        pre = []
        for i in range(s,e+1):
            if arr[i] > k:
                pre.append(arr[i])
        try:
            answer.append(min(pre))
        except:
            answer.append(-1)
    return answer