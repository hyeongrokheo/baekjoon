"""
problem tier : Silver 1 (solved.ac)
"""

# import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline
from copy import deepcopy

N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

max_count = 0

for C in range(101):
    new_arr = deepcopy(arr)
    count = 0
    for i in range(N):
        for j in range(N):
            if new_arr[i][j] > C:
                count += 1
                queue = [(i, j)]
                while len(queue) != 0:
                    x, y = queue.pop()
                    if new_arr[x][y] <= C:
                        continue
                    new_arr[x][y] = 0

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N and new_arr[nx][ny] > C:
                            queue.append((nx, ny))
    if max_count < count:
        max_count = count

print(max_count)
