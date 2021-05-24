"""
problem tier : Gold 4 (solved.ac)
"""

from copy import deepcopy


def mul(A, B):
    N = len(A)
    C = [[None for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            dot = 0
            for k in range(N):
                dot += A[i][k] * B[k][j]
            C[i][j] = dot % 1000
    # print(C)

    return C

# mul([[1,2],[3,4]], [[3,3],[2,5]])
# exit()

N, B = map(lambda x: int(x), input().split())

matrix = []
for i in range(N):
    matrix.append(list(map(lambda x: int(x), input().split())))

multiplier = deepcopy(matrix)
B = list(map(lambda x: int(x), str(bin(B))[2:]))
B.reverse()

result = []
for i in range(N):
    l = [0]*N
    l[i] = 1
    result.append(l)

for i in B:
    if i == 1:
        result = mul(result, multiplier)
    multiplier = mul(multiplier, multiplier)

for l in result:
    print(' '.join(map(str, l)))
