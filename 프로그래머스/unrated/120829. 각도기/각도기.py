def solution(angle):
    if angle <= 90:
        return angle // 90 + 1
    return angle // 90 + 2