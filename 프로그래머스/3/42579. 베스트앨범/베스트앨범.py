from collections import OrderedDict

def solution(genres, plays):
    answer = []
    genres_play = OrderedDict()
    songs = OrderedDict()
    
    for song,(g, p) in enumerate(zip(genres, plays)):
        if g not in genres_play:
            genres_play[g] = p
        elif g in genres_play:
            genres_play[g] += p
        if g not in songs:
            songs[g] = [[song,p]]
        elif g in songs:
            songs[g].append([song,p])
    genres_play = OrderedDict(sorted(genres_play.items(), key=lambda x:x[1], reverse=True))
    
    for i in genres_play:
        for j in range(2):
            try:
                answer.append([k[0] for k in sorted(songs[i], key=lambda x: x[1], reverse=True)][j])
            except:
                pass
    return answer