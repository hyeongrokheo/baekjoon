"""
problem tier : Gold 4 (solved.ac)
"""

import sys
sys.setrecursionlimit(10**8)
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

union_tree = [i for i in range(N)]

def find(x):
    if x == union_tree[x]:
        return x
    else:
        px = find(union_tree[x])
        union_tree[x] = px
        return px

def add(x, y):
    px, py = find(x), find(y)
    if px == py:
        False
    else:
        union_tree[py] = px
        return True

round = 0
for i in range(M):
    P1, P2 = map(int, input().split())
    if not round and not add(P1, P2):
        round = i+1
print(round)


