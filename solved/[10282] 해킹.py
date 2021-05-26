"""
problem tier : Gold 4 (solved.ac)
"""

import heapq
import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

INF = 999999999
T = int(input())

while T:
    T -= 1

    N, D, C = map(int, sys.stdin.readline().split())

    length = {}
    for i in range(D):
        a, b, s = map(int, sys.stdin.readline().split())
        if b not in length.keys():
            length[b] = {}
        length[b][a] = s
    # print(length)

    dist = [INF for i in range(N+1)]
    dist[C] = 0

    queue = []
    heapq.heappush(queue, (0, C))

    while len(queue) != 0:
        _, p = heapq.heappop(queue)

        if p in length.keys():
            for q in length[p].keys():
                if dist[q] > dist[p] + length[p][q]:
                    dist[q] = dist[p] + length[p][q]
                    heapq.heappush(queue, (dist[q], q))

    count = 0
    time = 0
    for d in dist:
        if d == INF:
            continue
        else:
            count += 1
            if time < d:
                time = d

    print(count, time)


