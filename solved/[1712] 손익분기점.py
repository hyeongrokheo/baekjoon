"""
problem tier : Bronze 4 (solved_old.ac)
"""

import math
inp = list(map(int, input().split(' ')))
A = inp[0]
B = inp[1]
C = inp[2]

if B >= C:
    print(-1)
else:
    print(int(math.ceil((A+1)/(C-B))))