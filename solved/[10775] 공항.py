"""
problem tier : Gold 2 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

G = int(input())
P = int(input())

union_tree = [i for i in range(G+1)]

def find_gate(x):
    if x == union_tree[x]:
        union_tree[x] -= 1
        return x
    else:
        px = union_tree[x]
        union_tree[x] = find_gate(px)
        return union_tree[x]

def update_gate(x):
    find_gate(x)

count = 0
for i in range(P):
    g = int(input())
    if find_gate(g) == 0:
        break
    count += 1

print(count)