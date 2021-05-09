"""
problem tier : Silver 2 (solved_old.ac)
"""

n, m = map(lambda x: int(x), input().split())

memo = [[None for j in range(m+1)] for i in range(n+1)]

def C(n, m):
    if m > n//2:
        m = n-m
    if memo[n][m]:
        return memo[n][m]

    if m == 1:
        memo[n][m] = n
    else:
        memo[n][m] = C(n-1, m) + C(n-1, m-1)

    return memo[n][m]

print(C(n, m))
