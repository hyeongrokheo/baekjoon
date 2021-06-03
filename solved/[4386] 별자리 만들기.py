"""
problem tier : Gold 4 (solved.ac)
"""

import heapq
import math
import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N = int(input())

union_tree = []
for i in range(N):
    union_tree.append(i)

def find(x):
    if x == union_tree[x]:
        return x
    else:
        px = find(union_tree[x])
        union_tree[x] = px
        return px

def add(x, y):
    px = find(x)
    py = find(y)
    if px != py:
        union_tree[py] = px

S = []
L = []
for i in range(N):
    x, y = map(float, input().split())
    for j in range(len(S)):
        dist = math.sqrt((S[j][0] - x) ** 2 + (S[j][1] - y) ** 2)
        heapq.heappush(L, (dist, j, i))
    S.append([x, y])

total_dist = 0
while len(L) > 0:
    dist, A, B = heapq.heappop(L)
    if find(A) != find(B):
        add(A, B)
        total_dist += dist
print('{:.2f}'.format(total_dist))
