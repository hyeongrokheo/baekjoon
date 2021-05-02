"""
problem tier : Gold 5 (solved_old.ac)
"""

import sys
from collections import deque

T = int(input())

while T:
    T -= 1
    opers = sys.stdin.readline().replace('RR', '')
    new_opers = []
    R_count = False
    for oper in opers:
        if oper == 'R':
            R_count = not R_count
        elif oper == 'D':
            if R_count:
                new_opers.append('R')
            else:
                new_opers.append('L')

    sys.stdin.readline()
    inp = sys.stdin.readline().strip().replace('[', '').replace(']', '')
    if inp == '':
        queue = deque()
    else:
        arr = list(map(lambda x: int(x), inp.split(',')))
        queue = deque(arr)
    error = False

    for oper in new_opers:
        if len(queue) == 0:
            error = True
            break
        if oper == 'R':
            if len(queue) == 0:
                error = True
                print('error')
            queue.pop()
        else:
            if len(queue) == 0:
                error = True
                print('error')
            queue.popleft()
    if R_count:
        queue.reverse()
    if not error:
        print('[', end='')
        print(','.join(map(str, list(queue))), end='')
        print(']')
    else:
        print('error')
