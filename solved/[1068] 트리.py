"""
problem tier : Gold 5 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

N = int(input())
parents = list(map(int, input().split()))
childs = [[] for i in range(N)]

for i in range(N):
    if parents[i] != -1:
        childs[parents[i]].append(i)

X = int(input())
S = [X]
while len(S) > 0:
    target = S.pop()
    if childs[target] == []:
        childs[target] = -1
    else:
        S.extend(childs[target])
        childs[target] = -1

if parents[X] == -1:
    print(0)
else:
    childs[parents[X]].remove(X)

    leaf_count = 0
    for c in childs:
        if c == []:
            leaf_count += 1

    print(leaf_count)