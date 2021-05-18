"""
problem tier : Silver 1 (solved_old.ac)
"""

from collections import deque

N = int(input())

# dp = [None for i in range(N+1)]

queue = deque()
queue.append([N])

memo = [False for i in range(N+1)]

while True:
    q = queue.popleft()
    n = q[-1]
    memo[n] = True
    if n == 1:
        print(len(q)-1)
        print(' '.join(map(lambda x: str(x), q)))
        break
    if n % 3 == 0 and not memo[n // 3]:
        queue.append(q + [n // 3])
    if n % 2 == 0 and not memo[n // 2]:
        queue.append(q + [n // 2])
    if not memo[n - 1]:
        queue.append(q + [n - 1])
