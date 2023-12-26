def solution(order):
    cnt = 0
    main_queue = order[0]
    sub_stack = [i for i in range(1,order[0])]
    for o in order:
        if o > main_queue:
            sub_stack += [i for i in range(main_queue,o)]
            main_queue = o
        if sub_stack and o == sub_stack[-1]:
            cnt += 1
            sub_stack.pop()
        elif o == main_queue:
            cnt += 1
            main_queue += 1
        else:
            return cnt
    return cnt
            