def solution(elements):
    lene = len(elements)
    set_ = set()
    for i in range(lene):
        for j in range(lene):
            set_.add(sum(elements[0:i+1]))
            elements.append(elements.pop(0))
    return len(set_)