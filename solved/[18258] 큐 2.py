"""
problem tier : Silver 4 (solved_old.ac)
"""

import sys
from collections import deque

N = int(input())

queue = deque()

while N:
    N -= 1

    # oper = input().split()
    oper = sys.stdin.readline().split()
    # print(oper)

    if oper[0] == 'push':
        queue.append(int(oper[1]))
    elif oper[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif oper[0] == 'size':
        print(len(queue))
    elif oper[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif oper[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif oper[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
