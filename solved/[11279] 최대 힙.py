"""
problem tier : Silver 2 (solved_old.ac)
"""

import heapq
import sys

queue = []
N = int(input())

for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(queue) == 0:
            print(0)
        else:
            print(heapq.heappop(queue)[1])
    else:
        heapq.heappush(queue, (-num, num))
