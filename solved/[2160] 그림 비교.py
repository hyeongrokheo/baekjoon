"""
problem tier : Bronze 1 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
PICTURE_SIZE = 35


def compare_picture(pic1, pic2):
    count = PICTURE_SIZE
    for i in range(PICTURE_SIZE):
        count -= pic1[i] == pic2[i]
    return count


def solution():
    N = int(input())

    pictures = []
    for _ in range(N):
        pic = input() + input() + input() + input() + input()
        pictures.append(pic)

    min_distance = PICTURE_SIZE + 1
    min_pics = None
    for i in range(N):
        for j in range(i + 1, N):
            distance = compare_picture(pictures[i], pictures[j])
            if min_distance > distance:
                min_distance = distance
                min_pics = (i+1, j+1)

    print(min_pics[0], min_pics[1])


solution()
