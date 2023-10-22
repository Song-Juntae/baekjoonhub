def solution(array):
    return sorted([[i,idx] for idx, i in enumerate(array)], key=lambda x: x[0])[-1]