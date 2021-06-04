"""
problem tier : Gold 4 (solved.ac)
"""

import sys
sys.setrecursionlimit(10**6)
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

union_tree = [i for i in range(N+1)]

def find(x):
    if x == union_tree[x]:
        return x
    else:
        px = find(union_tree[x])
        union_tree[x] = px
        return px

def merge(x, y):
    px = find(x)
    py = find(y)
    if px != py:
        union_tree[py] = px

for i in range(M):
    a, b, c = map(int, input().split())
    if a == 0:
        merge(b, c)
    else:
        if find(b) == find(c):
            print('YES')
        else:
            print('NO')
