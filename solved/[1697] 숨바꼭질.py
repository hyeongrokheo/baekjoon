"""
problem tier : Silver 1 (solved.ac)
"""

from collections import deque
import sys
sys.setrecursionlimit(10**8)

N, K = map(lambda x: int(x), input().split())

queue = deque()

queue.append([N, 0])
ancestor = [False for i in range(100001)]

while True:

    point = queue.popleft()
    ancestor[point[0]] = True
    if point[0] == K:
        print(point[1])
        break
    else:
        if point[0]-1 >= 0 and not ancestor[point[0]-1]:
            queue.append([point[0]-1, point[1]+1])
        if point[0]+1 <= 100000 and not ancestor[point[0]+1]:
            queue.append([point[0]+1, point[1]+1])
        if point[0]*2 <= 100000 and not ancestor[point[0]*2]:
            queue.append([point[0]*2, point[1]+1])
