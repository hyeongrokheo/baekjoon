"""
problem tier : Gold 4 (solved.ac)
"""

import sys
# sys.stdin = open('./../input.txt', 'r')
input = sys.stdin.readline

T = int(input())

def dfs(point):
    ancient = []
    depth = 1
    while True:
        if S[point][1] == 0:  # 방문안했음
            # visited[point] = True
            S[point][1] = depth
            depth += 1
            ancient.append(point)
            point = S[point][0]
        else:
            if visited[point]:  # 이전 여정에 방문했음. 그럼 탐색 끝
                for anc in ancient:
                    visited[anc] = True
                return depth-1
            else:  # 이번 여정에 방문했음. 사이클 만들어짐
                for anc in ancient:
                    visited[anc] = True
                return S[point][1]-1

while T:
    T -= 1
    N = int(input())
    S = list(map(lambda x: [int(x)-1, 0], input().split()))
    visited = [False for i in range(N)]
    done = [False for i in range(N)]
    # print(S)

    solo = 0

    for i in range(N):
        if S[i][1] == 0:
            solo += dfs(i)

    print(solo)
