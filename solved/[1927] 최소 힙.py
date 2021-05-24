"""
problem tier : Silver 1 (solved.ac)
"""

import sys, heapq

pri_queue = []

N = int(input())

for i in range(N):
    num = int(sys.stdin.readline())
    # print(num)

    if num == 0:
        if len(pri_queue) == 0:
            print(0)
        else:
            print(heapq.heappop(pri_queue))
    else:
        heapq.heappush(pri_queue, num)
