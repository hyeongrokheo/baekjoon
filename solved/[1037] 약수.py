"""
problem tier : Silver 5 (solved.ac)
"""

N = int(input())

div_N = list(map(lambda x: int(x), input().split()))
div_N.sort()

if N == 1:
    print(div_N[0] ** 2)
else:
    print(div_N[0] * div_N[-1])
