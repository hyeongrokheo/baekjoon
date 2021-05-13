"""
problem tier : Silver 2 (solved_old.ac)
"""

N = int(input())

A = list(map(lambda x: int(x), input().split()))
dp = [None] * N

for i in range(N):
    max_count = 0
    for j in range(i):
        if A[j] < A[i] and max_count < dp[j]:
            max_count = dp[j]
    dp[i] = max_count + 1

print(dp)
print(max(dp))
