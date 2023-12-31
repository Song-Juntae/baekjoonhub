def solution(bridge_length, weight, truck_weights):
    cnt = bridge_length
    b = [0]*bridge_length
    w = 0
    while truck_weights:
        cnt += 1
        popped = truck_weights[0]
        if b[0] == 0:
            del b[0]
            if w + popped <= weight:
                w += popped
                b.append(truck_weights.pop(0))
            else:
                b.append(0)
        else:
            w -= b[0]
            del b[0]
            if w + popped <= weight:
                w += popped
                b.append(truck_weights.pop(0))
            else:
                b.append(0)
    return cnt