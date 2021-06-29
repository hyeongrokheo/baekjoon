"""
problem tier : Unrated (solved.ac)
"""

import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N, P = map(int, input().split())
DC = [[], [], []]

for i in range(N):
    c, p = map(int, input().split())
    DC[p-1].append(c)

for i in range(3):
    DC[i].sort()

ancient = [[[False for i in range(51)] for j in range(51)] for k in range(51)]

min_cost = 1000000000
def DFS(p1, p2, p3, unt_cost, P):
    if ancient[p1][p2][p3]:
        return
    else:
        ancient[p1][p2][p3] = True

    global min_cost
    cost = unt_cost + P
    if min_cost > cost:
        min_cost = cost

    if p1 < len(DC[0]):
        DFS(p1+1, p2, p3, unt_cost+DC[0][p1], P*0.99)
    if p2 < len(DC[1]):
        DFS(p1, p2+1, p3, unt_cost+DC[1][p2], P*0.98)
    if p3 < len(DC[2]):
        DFS(p1, p2, p3+1, unt_cost+DC[2][p3], P*0.97)

DFS(0, 0, 0, 0, P)
print(min_cost)

