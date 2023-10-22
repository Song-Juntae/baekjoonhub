def solution(numbers):
    if len(numbers) == 2:
        return numbers[0]*numbers[1]
    return max(j*i for j in numbers for i in numbers if i!=j)