def solution(my_string, indices):
    for i in indices:
        my_string = my_string[:i] + ' ' + my_string[i+1:]
    return my_string.replace(' ','')