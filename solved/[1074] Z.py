"""
problem tier : Silver 1 (solved.ac)
"""


def Z(N, r, c):
    if N == 1:
        if r == 0 and c == 0:
            return 0
        elif r == 0 and c == 1:
            return 1
        elif r == 1 and c == 0:
            return 2
        else:
            return 3
    else:
        standard = 2**(N-1)
        if r < standard and c < standard:
            return Z(N-1, r, c)
        elif r < standard and c >= standard:
            return standard**2 + Z(N-1, r, c-standard)
        elif r >= standard and c < standard:
            return standard**2*2 + Z(N-1, r-standard, c)
        else:
            return standard**2*3 + Z(N-1, r-standard, c-standard)


N, r, c = map(lambda x: int(x), input().split())
print(Z(N, r, c))

