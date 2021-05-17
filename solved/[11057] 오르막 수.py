"""
problem tier : Silver 1 (solved_old.ac)
"""

N = int(input())
dp = [[0 for j in range(10)] for i in range(N)]
# print(dp)

dp[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, N):
    for j in range(10):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k] % 10007

print(sum(dp[-1]) % 10007)
