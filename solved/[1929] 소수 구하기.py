"""
problem tier : Silver 2 (solved_old.ac)
"""

import math

inp = input().split()
M = int(inp[0])
N = int(inp[1])

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

for i in range(len(pool)):
    if i < M:
        continue
    if pool[i]:
        print(i)