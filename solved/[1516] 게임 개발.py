"""
problem tier : Gold 3 (solved.ac)
"""

import heapq
import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

INF = 99999999
N = int(input())

building = [[None, 0, [], INF] for i in range(N)]

for i in range(N):
    inp = list(map(int, input().split()))
    building[i][0] = inp[0]
    for pre in inp[1:-1]:
        building[i][1] += 1
        building[pre-1][2].append(i)

Q = []

for i in range(N):
    if building[i][1] == 0:
        heapq.heappush(Q, (building[i][0], i))

while len(Q) > 0:
    time, target = heapq.heappop(Q)
    building[target][3] = time

    for next in building[target][2]:
        building[next][1] -= 1
        if building[next][1] == 0:
            heapq.heappush(Q, (building[target][3] + building[next][0], next))

for i in range(N):
    print(building[i][3])
