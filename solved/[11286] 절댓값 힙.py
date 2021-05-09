"""
problem tier : Silver 1 (solved_old.ac)
"""

import sys, heapq

pri_queue = []

N = int(input())

class node:
    def __init__(self, num):
        self.abs = abs(num)
        self.num = num

    def __lt__(self, other):
        if self.abs < other.abs:
            return True
        elif self.abs > other.abs:
            return False
        else:
            if self.num < other.num:
                return True
            else:
                return False

for i in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        if len(pri_queue) == 0:
            print(0)
        else:
            print(heapq.heappop(pri_queue).num)
    else:
        heapq.heappush(pri_queue, node(num))
