"""
problem tier : Gold 5 (solved_old.ac)
"""

import sys
sys.setrecursionlimit(10**8)

N = int(input())
picture_1 = []
picture_2 = []

for i in range(N):
    line = list(input())
    picture_1.append(line)

    line = list(map(lambda x: 'R' if x == 'G' else x, line))
    picture_2.append(line)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def search(pic, x, y):
    color = pic[x][y]
    pic[x][y] = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < N and 0 <= ny < N and pic[nx][ny] == color:
            search(pic, nx, ny)

pic1_count = 0
pic2_count = 0
for i in range(N):
    for j in range(N):
        if picture_1[i][j] != 0:
            search(picture_1, i, j)
            pic1_count += 1
        if picture_2[i][j] != 0:
            search(picture_2, i, j)
            pic2_count += 1


print(pic1_count, pic2_count)
