"""
코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [3차] 방금그곡
"""
"""
C, D, E, F, G, A, B
A# H
C# I
D# J
F# K
G# L
"""
def solution(m, musicinfos):
    target_melody = m
    target_melody = target_melody.replace('A#', 'H')
    target_melody = target_melody.replace('C#', 'I')
    target_melody = target_melody.replace('D#', 'J')
    target_melody = target_melody.replace('F#', 'K')
    target_melody = target_melody.replace('G#', 'L')
    prior = 0
    correct_musics = []
    for musicinfo in musicinfos:
        start, end, name, melody = musicinfo.split(',')
        start = int(start.split(':')[0])*60 + int(start.split(':')[1])
        end = int(end.split(':')[0])*60 + int(end.split(':')[1])
        melody = melody.replace('A#', 'H')
        melody = melody.replace('C#', 'I')
        melody = melody.replace('D#', 'J')
        melody = melody.replace('F#', 'K')
        melody = melody.replace('G#', 'L')

        duration = end-start

        melody_in_duration = ''
        while len(melody_in_duration) < duration:
            melody_in_duration += melody
        melody_in_duration = melody_in_duration[:duration]
        if target_melody in melody_in_duration:
            correct_musics.append([duration, prior, name])
        prior += 1
    correct_musics.sort(key=lambda x: (-x[0], x[1]))
    if len(correct_musics) != 0:
        return correct_musics[0][2]
    else:
        return '(None)'


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
