"""
코딩테스트 연습 > 해시
"""


def solution(genres, plays):
    genres_map = {}
    for i in range(len(genres)):
        d = (i, plays[i])
        if genres[i] in genres_map.keys():
            genres_map[genres[i]].append(d)
        else:
            genres_map[genres[i]] = [d]

    data = []
    for musics in genres_map.values():
        genres_play = 0
        for m in musics:
            genres_play += m[1]

        musics.sort(key=lambda x: -x[1])

        if len(musics) > 2:
            musics = musics[:2]
        for m in musics:
            data.append((m[0], genres_play, m[1]))

    data.sort(key=lambda x: (-x[1], -x[2], x[0]))

    return list(map(lambda x: x[0], data))

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
