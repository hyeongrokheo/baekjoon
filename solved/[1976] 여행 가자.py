"""
problem tier : Gold 4 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

N = int(input())
M = int(input())

union_tree = [i for i in range(N)]

def find(x):
    if x == union_tree[x]:
        return x
    else:
        px = union_tree[x]
        union_tree[x] = find(px)
        return union_tree[x]

def merge(x, y):
    px, py = find(x), find(y)
    if px != py:
        union_tree[px] = py

connected = []
for i in range(N):
    m = list(map(int, input().split()))
    for j in range(N):
        if m[j] == 1:
            merge(i, j)

plan = list(map(int, input().split()))

# print(union_tree)
answer = 'YES'
for p in plan:
    if find(p-1) != find(plan[0]-1):
        answer = 'NO'
        break

# print(find(0))
print(answer)
