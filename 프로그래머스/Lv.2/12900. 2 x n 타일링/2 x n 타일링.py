def solution(n):
    if n == 1:
        return 1
    pre = 1
    post = 1
    for i in range(n-1):
        _ = pre + post
        pre = post
        post = _
    return post % 1000000007