def solution(n, arr1, arr2):
    return [str(int(format(i, 'b'))+int(format(j, 'b'))).zfill(n).replace('0',' ').replace('1','#').replace('2','#') for i,j in zip(arr1,arr2)]