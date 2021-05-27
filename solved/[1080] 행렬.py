"""
problem tier : Silver 2 (solved.ac)
"""

# import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())

A = []
B = []
C = [[None for j in range(M)] for i in range(N)]

for i in range(N):
    A.append(list(map(str, input())))
for i in range(N):
    B.append(list(map(str, input())))
for i in range(N):
    for j in range(M):
        if A[i][j] == B[i][j]:
            C[i][j] = False
        else:
            C[i][j] = True

# for c in C:
#     print(c)

dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

count = 0
for i in range(1, N-1):
    for j in range(1, M-1):
        if C[i-1][j-1]:
            # print(i, j)
            for k in range(9):
                C[i+dx[k]][j+dy[k]] = not C[i+dx[k]][j+dy[k]]
            count += 1

# print()
# for c in C:
#     print(c)
success = True
for i in range(N):
    for j in range(M):
        if C[i][j]:
            success = False
if success:
    print(count)
else:
    print(-1)
