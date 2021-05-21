"""
problem tier : Silver 1 (solved_old.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

INF = 999999999
T = int(sys.stdin.readline())

while T:
    T -= 1

    N = int(sys.stdin.readline())
    dist = [[INF for j in range(N+2)] for i in range(N+2)]
    for i in range(N+2):
        dist[i][i] = 0

    store = []
    store.append(list(map(lambda x: int(x), sys.stdin.readline().split())))
    for i in range(N):
        x, y = map(lambda x: int(x), sys.stdin.readline().split())
        store.append([x, y])
    store.append(list(map(lambda x: int(x), sys.stdin.readline().split())))

    for i in range(N+2):
        for j in range(N+2):
            if i == j:
                dist[i][j] = 0
            else:
                dist[i][j] = 1 if abs(store[i][0] - store[j][0]) + abs(store[i][1] - store[j][1]) <= 1000 else INF

    for m in range(N+2):
        for s in range(N+2):
            for e in range(N+2):
                if dist[s][e] > dist[s][m] + dist[m][e]:
                    dist[s][e] = dist[s][m] + dist[m][e]
    # for d in dist:
    #     print(d)
    # print()

    if dist[0][N+1] == INF:
        print('sad')
    else:
        print('happy')

