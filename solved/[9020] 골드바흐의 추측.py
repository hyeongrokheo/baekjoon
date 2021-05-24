"""
problem tier : Silver 1 (solved.ac)
"""

import math

T = int(input())
M = 1
N = 10000

pool = [True] * (N+1)
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

while T:
    T -= 1

    n = int(input())
    partition = int(n/2)
    while True:
        # print(partition)
        if pool[partition] and pool[n - partition]:
            print(partition, n-partition)
            break
        partition -= 1
