"""
problem tier : Gold 3 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

dp = [[0 for j in range(N)] for i in range(N)]

for i in range(N+1):
    for j in range(i):
        x = N-i
        y = x+j
        # print(x, y)
        if x == y:
            dp[x][y] = 1
        elif num[x] == num[y]:
            if y - x <= 1:
                dp[x][y] = 1
            else:
                dp[x][y] = dp[x+1][y-1]
        # else:
        #     dp[x][y] = 0

# for d in dp:
#     print(d)

M = int(input())
for i in range(M):
    a, b = map(int, input().split())
    print(dp[a-1][b-1])
