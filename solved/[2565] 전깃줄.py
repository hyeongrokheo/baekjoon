"""
problem tier : Silver 1 (solved_old.ac)
"""

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(lambda x: int(x), input().split())))

arr.sort(key=lambda x: x[0])
arr = list(map(lambda x: x[1], arr))
# print(arr)

left, right = 0, N-1
dp = [None for i in range(N)]

for i in range(N):
    max_len = 0
    for j in range(i):
        if arr[j] < arr[i] and max_len < dp[j]:
            max_len = dp[j]
    dp[i] = max_len + 1

print(N - max(dp))
