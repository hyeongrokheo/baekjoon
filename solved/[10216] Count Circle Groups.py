"""
problem tier : Gold 5 (solved.ac)
"""

import math
import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

T = int(input())

while T:
    T -= 1
    N = int(input())
    groups = []
    for i in range(N):
        x, y, r = map(int, input().split())
        groups.append([x, y, r])

    connected = [[] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            else:
                if groups[i][2] + groups[j][2] >= math.sqrt((groups[i][0] - groups[j][0]) ** 2 + (groups[i][1] - groups[j][1]) ** 2):
                    connected[i].append(j)

    visited = [False for i in range(N)]
    count = 0
    for i in range(N):
        if not visited[i]:
            count += 1
            stack = [i]

            while len(stack) != 0:
                p = stack.pop()
                if visited[p]:
                    continue
                visited[p] = True
                for next in connected[p]:
                    if not visited[next]:
                        stack.append(next)
    print(count)
