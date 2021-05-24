"""
problem tier : Silver 2 (solved.ac)
"""

import sys
sys.setrecursionlimit(10**8)

N, M = map(lambda x: int(x), input().split())

E = {}
# print(E)

for i in range(M):
    V1, V2 = map(lambda x: int(x), sys.stdin.readline().split())
    if V1 not in E.keys():
        E[V1] = []
    E[V1].append(V2)
    if V2 not in E.keys():
        E[V2] = []
    E[V2].append(V1)

# print(E)
# exit()
V = [False for i in range(N+1)]

def connect(v):
    V[v] = True
    if v in E.keys():
        for i in E[v]:
            if not V[i]:
                connect(i)


count = 0
for i in range(1, N+1):
    if not V[i]:
        connect(i)
        count += 1

print(count)
