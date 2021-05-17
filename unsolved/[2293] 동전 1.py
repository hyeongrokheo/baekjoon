"""
problem tier : Silver 1 (solved_old.ac)
"""

n, k = map(lambda x: int(x), input().split())
coin = list(map(lambda x: int(x), input().split()))

dp = [[0 for j in range(k)] for i in range(n)]

