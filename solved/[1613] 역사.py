"""
problem tier : Gold 3 (solved_old.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

INF = 9999999
# print(input)
n, k = map(lambda x: int(x), input().split())

first = [[INF for j in range(n)] for i in range(n)]
afterwards = [[INF for j in range(n)] for i in range(n)]

for i in range(n):
    first[i][i] = 0
    afterwards[i][i] = 0

for i in range(k):
    f, a = map(lambda x: int(x), sys.stdin.readline().split())
    first[f-1][a-1] = 1
    afterwards[a-1][f-1] = 1

for m in range(n):
    for s in range(n):
        for e in range(n):
            if first[s][e] > first[s][m] + first[m][e]:
                first[s][e] = first[s][m] + first[m][e]
            if afterwards[s][e] > afterwards[s][m] + afterwards[m][e]:
                afterwards[s][e] = afterwards[s][m] + afterwards[m][e]

s = int(input())
for i in range(s):
    e1, e2 = map(lambda x: int(x), sys.stdin.readline().split())
    if first[e1-1][e2-1] != INF:
        print(-1)
    elif afterwards[e1-1][e2-1] != INF:
        print(1)
    else:
        print(0)
