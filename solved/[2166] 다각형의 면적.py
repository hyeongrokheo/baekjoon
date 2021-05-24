"""
problem tier : Gold 5 (solved.ac)
"""

N = int(input())

V = []
for i in range(N):
    V.append(list(map(lambda x: int(x), input().split())))
V.append(V[0])

S = 0
for i in range(N):
    S += V[i][0] * V[i+1][1]
    S -= V[i+1][0] * V[i][1]


S = abs(S / 2)
print(S)
