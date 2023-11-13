def solution(food):
    _ = ''.join(f'{idx}'*(i//2) for idx,i in enumerate(food))
    return _ + '0' + _[::-1]