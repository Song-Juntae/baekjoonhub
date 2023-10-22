def solution(my_string):
    _ = []
    for i in my_string:
        if i not in _:
            _.append(i)
    return ''.join(_)