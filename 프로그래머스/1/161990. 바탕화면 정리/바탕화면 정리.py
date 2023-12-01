def solution(wallpaper):
    min_x, min_y = 51, 51
    max_x, max_y = 0, 0
    for idx, i in enumerate(wallpaper):
        if '#' in i:
            min_ = i.find('#')
            max_ = i.rfind('#')
            min_x, min_y = min(min_x,min_), min(min_y,idx)
            max_x, max_y = max(max_x,max_), max(max_y,idx)
    return [min_y, min_x, max_y+1, max_x+1]