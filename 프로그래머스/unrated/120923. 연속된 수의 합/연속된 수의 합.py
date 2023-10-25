def solution(num, total):
    return [idx+i for idx,i in enumerate([(total - sum(range(num)))/num] * num)]
        