"""
problem tier : Gold 4 (solved.ac)
"""

import sys
input = sys.stdin.readline

V, E = map(int, input().split())

edges = []

for i in range(E):
    A, B, C, = map(int, input().split())
    edges.append((A, B, C))

edges.sort(key=lambda x: x[2])

length = 0
groups = []
for e in edges:
    A, B, C = e
    A_group = -1
    B_group = -1
    for i in range(len(groups)):
        if A in groups[i]:
            A_group = i
        if B in groups[i]:
            B_group = i
    if A_group == -1 and B_group == -1:
        groups.append(set([A, B]))
        length += C
    elif A_group == -1 and B_group != -1:
        groups[B_group].add(A)
        length += C
    elif A_group != -1 and B_group == -1:
        groups[A_group].add(B)
        length += C
    else:
        if A_group != B_group:
            groups[A_group] = groups[A_group].union(groups[B_group])
            groups.pop(B_group)
            length += C

print(length)
