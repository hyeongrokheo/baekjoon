"""
problem tier : Bronze 2 (solved.ac)
"""


def DecompositionSum(N):
    S = N
    while N >= 1:
        S += N % 10
        N //= 10
    return S


N = int(input())
flag = False
for i in range(N - len(str(N)) * 9, N):
    if DecompositionSum(i) == N:
        print(i)
        flag = True
        break
if not flag:
    print(0)
