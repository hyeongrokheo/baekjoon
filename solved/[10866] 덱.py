"""
problem tier : Silver 4 (solved_old.ac)
"""

from collections import deque
import sys

Deque = deque()

N = int(input())

while N:
    N -= 1

    # oper = input().split()
    oper = sys.stdin.readline().split()
    # print(oper)

    if oper[0] == 'push_front':
        Deque.appendleft(int(oper[1]))
    elif oper[0] == 'push_back':
        Deque.append(int(oper[1]))
    elif oper[0] == 'pop_front':
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque.popleft())
    elif oper[0] == 'pop_back':
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque.pop())
    elif oper[0] == 'size':
        print(len(Deque))
    elif oper[0] == 'empty':
        if len(Deque) == 0:
            print(1)
        else:
            print(0)
    elif oper[0] == 'front':
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[0])
    elif oper[0] == 'back':
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[-1])
