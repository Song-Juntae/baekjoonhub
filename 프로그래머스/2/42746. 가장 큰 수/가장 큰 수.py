def solution(numbers):
    if set(numbers) == set([0]):
        return '0'
    return ''.join(sorted([str(i) for i in numbers], key=lambda x: x*4, reverse=True))