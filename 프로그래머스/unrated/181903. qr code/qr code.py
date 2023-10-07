def solution(q, r, code):
    return "".join([i for idx, i in enumerate(code) if idx % q == r])