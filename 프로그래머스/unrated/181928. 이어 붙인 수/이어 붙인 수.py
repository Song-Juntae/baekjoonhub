def solution(num_list):
    홀수 = ''
    짝수 = ''
    for i in num_list:
        if i % 2 == 0 : 
            짝수 = 짝수 + str(i)
        else : 
            홀수 = 홀수 + str(i)
    return int(홀수)+int(짝수)