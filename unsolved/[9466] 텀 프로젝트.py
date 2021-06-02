"""
problem tier : Gold 4 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

T = int(input())

def dfs(p):
    ancient = []
    cycle = []

    while True:
        if p in ancient:
            flag = False
            for anc in ancient:
                if p == anc:
                    flag = True
                if flag:
                    cycle.append(anc)
            break
        elif visited[p]:
            return ancient, cycle
        else:
            ancient.append(p)
            p = S[p]

    return ancient, cycle

while T:
    T -= 1
    N = int(input())
    S = list(map(lambda x: int(x)-1, input().split()))
    visited = [False for i in range(N)]
    group = []

    for i in range(N):
        if visited[i]:
            continue

        ancient, cycle = dfs(i)
        for anc in ancient:
            visited[anc] = True
        for c in cycle:
            visited[c] = True
            group.append(c)

    print(N-len(group))
