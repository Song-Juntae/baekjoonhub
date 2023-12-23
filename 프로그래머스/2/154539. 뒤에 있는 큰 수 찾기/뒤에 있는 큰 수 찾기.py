def solution(numbers):
    answer = [-1]
    stack = [numbers[-1]]
    for n in reversed(numbers):
        for s in reversed(stack):
            if n < s:
                answer.append(s)
                stack.append(n)
                break
            else:
                stack.pop(-1)
        else:
            answer.append(-1)
            stack = [n]
    return [i for i in reversed(answer)][:-1]