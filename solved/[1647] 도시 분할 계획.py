"""
problem tier : Gold 4 (solved.ac)
"""

import sys
# sys.stdin = open('./../input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
roads = []
for i in range(M):
    A, B, C = map(int, input().split())
    roads.append((A, B, C))

roads.sort(key=lambda x: x[2])

union_tree = [i for i in range(N+1)]
def find(x):
    if x == union_tree[x]:
        return x
    else:
        px = find(union_tree[x])
        union_tree[x] = px
        return px

def add(x, y):
    px, py = find(x), find(y)
    if px != py:
        union_tree[px] = py
        return True
    else:
        return False

total_length = 0
max_length = 0
for road in roads:
    A, B, C = road
    if add(A, B):
        total_length += C
        if max_length < C:
            max_length = C

print(total_length - max_length)
