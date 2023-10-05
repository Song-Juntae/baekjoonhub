def solution(arr):
    try: 
        if arr[-1] == 2:
            return arr[arr.index(2):]
        return arr[arr.index(2):-(arr[::-1].index(2))]
    except:
        return [-1]