"""
problem tier : Gold 5 (solved_old.ac)
"""

import sys

N, K = map(lambda x: int(x), input().split())

item = []
for i in range(N):
    item.append(list(map(lambda x: int(x), sys.stdin.readline().split())))

item.sort(key=lambda x: x[0])
# print(item)

dp = [[None for j in range(K+1)] for i in range(len(item))]

# print(dp)

for i in range(len(item)):
    w, v = item[i][0], item[i][1]
    # print('w, v :', w, v)
    for j in range(K+1):
        # print('i, j :', i, j)
        if w > j:
            if i-1 >= 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = 0
        else:
            if i-1 >= 0:
                dp[i][j] = max(dp[i-1][j-w]+v, dp[i-1][j])
            else:
                dp[i][j] = v


print(dp[N-1][K])
# print(max(dp))
