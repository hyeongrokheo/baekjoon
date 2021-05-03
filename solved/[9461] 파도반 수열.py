"""
problem tier : Silver 3 (solved_old.ac)
"""

T = int(input())

while T:
    T -= 1

    a, b, c, d, e = 1, 1, 1, 2, 2
    N = int(input())
    for i in range(N-1):
        a, b, c, d, e = b, c, d, e, a+e
    # print(a, b, c, d, e)
    print(a)

