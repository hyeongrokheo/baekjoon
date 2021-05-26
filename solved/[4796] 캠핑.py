"""
problem tier : Silver 5 (solved.ac)
"""

T = 0
while True:
    T += 1
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break

    print('Case {}: {}'.format(T, (V // P) * L + min((V % P), L)))
