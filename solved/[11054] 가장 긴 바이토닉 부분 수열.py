"""
problem tier : Gold 3 (solved.ac)
"""

N = int(input())

A = list(map(lambda x: int(x), input().split()))
dp1 = [None] * N
dp2 = [None] * N

for i in range(N):
    max_count = 0
    for j in range(i):
        if A[j] < A[i] and max_count < dp1[j]:
            max_count = dp1[j]
    dp1[i] = max_count + 1

A.reverse()
# print(A)

for i in range(N):
    # print('i:', i)
    max_count = 0
    for j in range(i):
        if A[j] < A[i] and max_count < dp2[j]:
            max_count = dp2[j]
    dp2[i] = max_count + 1
    # print('dp2[i]:', dp2[i])
dp2.reverse()

# print(dp1)
dp = []
for i in range(N):
    dp.append(dp1[i]+dp2[i])
print(max(dp)-1)
