"""
problem tier : Gold 4 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

INF = 999999999
N = int(input())
houses = []
for i in range(N):
    houses.append(list(map(int, input().split())))

min_length = INF
for i in range(3):
    dp = [[INF, INF, INF] for i in range(N)]
    dp[0][i] = houses[0][i]
    if i > 0:
        dp[0][i-1] = INF
    for j in range(1, N-1):
        if min(dp[j-1][1], dp[j-1][2]) != INF:
            dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + houses[j][0]
        if min(dp[j-1][0], dp[j-1][2]) != INF:
            dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + houses[j][1]
        if min(dp[j-1][0], dp[j-1][1]) != INF:
            dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + houses[j][2]
    if i == 0:
        dp[N-1][1] = min(dp[N-2][2], dp[N-2][0]) + houses[N-1][1]
        dp[N-1][2] = min(dp[N-2][1], dp[N-2][0]) + houses[N-1][2]
    elif i == 1:
        dp[N-1][0] = min(dp[N-2][2], dp[N-2][1]) + houses[N-1][0]
        dp[N-1][2] = min(dp[N-2][0], dp[N-2][1]) + houses[N-1][2]
    else:
        dp[N-1][0] = min(dp[N-2][1], dp[N-2][2]) + houses[N-1][0]
        dp[N-1][1] = min(dp[N-2][0], dp[N-2][2]) + houses[N-1][1]

    if min_length > min(dp[-1]):
        min_length = min(dp[-1])

print(min_length)
