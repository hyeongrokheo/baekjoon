"""
problem tier : Silver 1 (solved_old.ac)
"""

from collections import deque
import sys
sys.setrecursionlimit(1000000)

N, M = map(lambda x: int(x), input().split())

maps = []
for i in range(N):
    maps.append(list(map(lambda x: int(x), sys.stdin.readline().strip())))

ancestor = [[False for j in range(M)] for i in range(N)]

def get_adj_list(x, y):
    adj_list = []
    if x > 0 and not ancestor[x-1][y] and maps[x-1][y] == 1:
        adj_list.append([x-1, y])
    if y > 0 and not ancestor[x][y-1] and maps[x][y-1] == 1:
        adj_list.append([x, y-1])
    if x < N-1 and not ancestor[x+1][y] and maps[x+1][y] == 1:
        adj_list.append([x+1, y])
    if y < M-1 and not ancestor[x][y+1] and maps[x][y+1] == 1:
        adj_list.append([x, y+1])
    return adj_list


queue = deque()
queue.append([0, 0, 1])
ancestor[0][0] = True

while True:
    nextNode = queue.popleft()
    x, y, length = nextNode[0], nextNode[1], nextNode[2]

    for adj in get_adj_list(x, y):
        if adj[0] == N-1 and adj[1] == M-1:
            print(length + 1)
            exit()
        else:
            adj.append(length + 1)
            ancestor[adj[0]][adj[1]] = True
            queue.append(adj)

