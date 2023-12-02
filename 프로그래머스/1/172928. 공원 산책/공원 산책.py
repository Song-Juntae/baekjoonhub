def solution(park, routes):
    dic_map = {}
    start = []
    for H, i in enumerate(park):
        for W, s in enumerate(i):
            dic_map[(H,W)] = s
            if s == 'S':
                start = [H,W]
    for r in routes:
        command = r.split(' ')
        _ = int(command[1])
        if command[0] == 'W':
            move = True
            for i in range(1,_+1):
                if (start[0],start[1]-i) not in dic_map:
                    move = False
                elif dic_map[(start[0],start[1]-i)] == 'X':
                    move = False
            if move:
                start = [start[0],start[1]-_]
                
        elif command[0] == 'E':
            move = True
            for i in range(1,_+1):
                if (start[0],start[1]+i) not in dic_map:
                    move = False
                elif dic_map[(start[0],start[1]+i)] == 'X':
                    move = False
            if move:
                start = [start[0],start[1]+_]
                
        elif command[0] == 'N':
            move = True
            for i in range(1,_+1):
                if (start[0]-i,start[1]) not in dic_map:
                    move = False
                elif dic_map[(start[0]-i,start[1])] == 'X':
                    move = False
            if move:
                start = [start[0]-_,start[1]]
        
        elif command[0] == 'S':
            move = True
            for i in range(1,_+1):
                if (start[0]+i,start[1]) not in dic_map:
                    move = False
                elif dic_map[(start[0]+i,start[1])] == 'X':
                    move = False
            if move:
                start = [start[0]+_,start[1]]
    return start