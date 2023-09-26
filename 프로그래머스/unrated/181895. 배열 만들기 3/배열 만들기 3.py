def solution(arr, intervals):
    
    return [j for i in intervals for j in arr[i[0]:i[1]+1]]