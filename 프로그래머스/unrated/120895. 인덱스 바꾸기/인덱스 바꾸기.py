def solution(my_string, num1, num2):
    i1,i2 = min(num1,num2),max(num1,num2)
    n1,n2 = my_string[i1],my_string[i2]
    return my_string[:i1]+n2+my_string[i1+1:i2]+n1+my_string[i2+1:]