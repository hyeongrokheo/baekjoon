"""
problem tier : Silver 1 (solved.ac)
"""

N = int(input())
P = list(map(lambda x: int(x), input().split()))

dp = [0 for i in range(N+1)]

for i in range(N+1):
    for j in range(len(P)):
        if i > j:
            # print(dp)
            # print(i, j)
            # print(dp[i], dp[i-j-1], P[j])
            if dp[i] < dp[i-j-1] + P[j]:
                dp[i] = dp[i-j-1] + P[j]

print(dp[-1])


