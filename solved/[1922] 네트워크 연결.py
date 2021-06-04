"""
problem tier : Gold 4 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

N = int(input())
M = int(input())

union_tree = [i for i in range(N+1)]

def find(x):
    if x == union_tree[x]:
        return x
    else:
        px = find(union_tree[x])
        union_tree[x] = px
        return px

def merge(x, y):
    px, py = find(x), find(y)
    if px != py:
        union_tree[py] = px


networks = []
for i in range(M):
    a, b, c = map(int, input().split())
    networks.append([a, b, c])
networks.sort(key=lambda x: x[2])

total_cost = 0
for network in networks:
    x, y, cost = network[0], network[1], network[2]
    if find(x) != find(y):
        total_cost += cost
        merge(x, y)

print(total_cost)
