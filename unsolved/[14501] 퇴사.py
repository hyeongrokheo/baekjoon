"""
problem tier : Silver 4 (solved_old.ac)
"""

import sys

N = int(input())
time = []
benefit = []
for i in range(N):
    t, b = map(lambda x: int(x), sys.stdin.readline().split())
    if i + t > N:
        b = 0
    time.append(t)
    benefit.append(b)

time.reverse()
benefit.reverse()

dp = [0 for i in range(N)]

for i in range(N):
    if i == 0:
        dp[i] = benefit[0]
    else:
        if i-time[i] >= 0:
            dp[i] = max(dp[i-time[i]] + benefit[i], dp[i-1])
        else:
            dp[i] = dp[i-1]

print(max(dp))
