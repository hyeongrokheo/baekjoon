"""
problem tier : Gold 3 (solved.ac)
"""

import math
import sys

input = sys.stdin.readline
N = int(input())
if N == 1:
    print(0)
    exit()

pool = [True for i in range(N+1)]
pool[0] = False
pool[1] = False

sqrt_N = math.ceil(math.sqrt(N))
for i in range(sqrt_N + 1):
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

prime_list = []
for i in range(1, len(pool)):
    if pool[i]:
        prime_list.append(i)

prime_len = len(prime_list)

left, right = 0, 0
prime_sum = prime_list[0]
count = 0
while True:
    if prime_sum == N:
        count += 1

    if prime_sum >= N:
        prime_sum -= prime_list[left]
        left += 1
    else:
        if right == prime_len-1:
            break
        prime_sum += prime_list[right+1]
        right += 1

print(count)
