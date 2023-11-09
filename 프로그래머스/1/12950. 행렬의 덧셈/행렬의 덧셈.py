def solution(arr1, arr2):
    answer = []
    for i,j in zip(arr1, arr2):
        _ = []
        for k,l in zip(i,j):
            _.append(k+l)
        answer.append(_)
    return answer