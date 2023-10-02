def solution(arr, flag):
    answer = []
    for idx, i in enumerate(flag):
        if i == True:
            answer += [arr[idx]]*(arr[idx]*2)
        else:
            answer = answer[:-arr[idx]]
    return answer