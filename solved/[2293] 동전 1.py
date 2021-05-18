"""
problem tier : Silver 1 (solved_old.ac)
"""

import sys

n, k = map(lambda x: int(x), input().split())
coin = []
for i in range(n):
    c = int(sys.stdin.readline())
    if c > k:
        n -= 1
        continue
    else:
        coin.append(c)

dp = [0 for j in range(k+1)]
dp[0] = 1
for i in range(n):
    for j in range(1, k+1):
        if i == 0:
            if j % coin[i] == 0:
                dp[j] = 1
        else:
            if j >= coin[i]:
                dp[j] += dp[j-coin[i]]
print(dp[k])
