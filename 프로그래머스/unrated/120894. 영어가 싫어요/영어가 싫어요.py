def solution(numbers):
    for idx,i in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(i,str(idx))
    return int(numbers)