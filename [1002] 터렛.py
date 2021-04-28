"""
problem tier : Silver 4 (solved.ac)
"""

import math

T = int(input())

while T:
    T -= 1

    x1, y1, r1, x2, y2, r2 = map(lambda x: int(x), input().split())

    if (x1, y1) == (x2, y2):
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if distance > r1+r2 or distance < abs(r1-r2):
            print(0)
        elif distance == r1+r2 or distance == abs(r1-r2):
            print(1)
        else:
            print(2)
