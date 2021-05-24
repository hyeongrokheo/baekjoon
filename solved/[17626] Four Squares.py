"""
problem tier : Silver 5 (solved.ac)
pypy3
"""

import math

n = int(input())

def FS(n, d, l):
    # print(n, d, l)
    if n == 0:
        print(l)
        return True

    if d < 4:
        for i in range(int(math.sqrt(n))+1):
            if i == 0:
                if FS(n-i**2, d+1, l):
                    return True
            else:
                if FS(n-i**2, d+1, l+1):
                    return True

FS(n, 0, 0)
