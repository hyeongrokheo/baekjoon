"""
problem tier : Gold 1 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

INF = 999999999
N = int(input())
costs = []
for i in range(N):
    costs.append(list(map(int, input().split())))

DP = [[INF for j in range(2**N)] for i in range(N)]


def DFS(node, bits, cost):
    if DP[node][bits] <= cost:
        return

    DP[node][bits] = cost

    for i in range(N):
        if costs[node][i] != 0 and not (bits & 2**i):
            DFS(i, bits+2**i, cost + costs[node][i])


DFS(0, 0, 0)

min_cost = INF
for i in range(N):
    if min_cost > DP[i][2**N-1]:
        min_cost = DP[i][2**N-1]
print(min_cost)
