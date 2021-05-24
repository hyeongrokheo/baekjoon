"""
problem tier : Silver 2 (solved.ac)
"""

import math
#1929번 코드 활용


def pr(M, N):
    pool = [True]*(N+1)
    pool[0] = False
    pool[1] = False

    for i in range(math.ceil(math.sqrt(N)) + 1):
        if i < 2:
            continue
        if not pool[i]:
            continue
        mul = 2
        while True:
            if i * mul > N:
                break
            else:
                pool[i * mul] = False
                mul += 1

    num = 0
    for i in range(len(pool)):
        if i < M:
            continue
        if pool[i]:
            num += 1
    return num


while True:
    inp = int(input())
    if inp == 0:
        break
    else:
        print(pr(inp+1, inp*2))