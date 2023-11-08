def solution(price, money, count):
    _ = sum(i for i in range(price,count*price+1,price)) - money
    if _ < 0:
        return 0
    return _