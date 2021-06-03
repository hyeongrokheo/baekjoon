"""
problem tier : Gold 2 (solved.ac)
"""

from copy import deepcopy
from collections import deque
import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

maps = []
for i in range(N):
    maps.append(list(input().strip()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

Q = deque()
Q.append((maps, 0))

while len(Q) > 0:
    origin_maps, depth = Q.popleft()

    for i in range(4):
        maps = deepcopy(origin_maps)
        for j in range(N):
            for k in range(M):
                if maps[j][k] == 'R':
                    red = [j, k]
                if maps[j][k] == 'B':
                    blue = [j, k]

        if maps[red[0]+dx[i]][red[1]+dy[i]] in ['B', '#'] and maps[blue[0]+dx[i]][blue[1]+dy[i]] in ['R', '#']:
            continue

        order = [0, 1]
        temp_red = deepcopy(red)
        while True:
            temp_red[0] += dx[i]
            temp_red[1] += dy[i]
            if temp_red[0] == blue[0] and temp_red[1] == blue[1]:
                order = [1, 0]
                break
            if maps[temp_red[0]][temp_red[1]] in ['#', 'O']:
                break

        goal = [False, True]
        for j in range(2):
            if order[j] == 0:
                current_ball = red
                current_ball_char = 'R'
            else:
                current_ball = blue
                current_ball_char = 'B'

            maps[current_ball[0]][current_ball[1]] = '.'
            while True:
                if maps[current_ball[0] + dx[i]][current_ball[1] + dy[i]] == '.':
                    current_ball[0] += dx[i]
                    current_ball[1] += dy[i]
                elif maps[current_ball[0] + dx[i]][current_ball[1] + dy[i]] == 'O':
                    if current_ball_char == 'R':
                        current_ball = [0, 0]
                        goal[0] = True
                    if current_ball_char == 'B':
                        goal[1] = False
                    break
                else:
                    break
            maps[current_ball[0]][current_ball[1]] = current_ball_char
        if goal[1] == True:
            if goal[0] == True:
                print(depth+1)
                exit()
            else:
                if depth < 9:
                    Q.append((maps, depth+1))

print(-1)
