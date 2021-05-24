"""
problem tier : Silver 4 (solved.ac)
"""

import sys
# sys.stdin = open('./../input.txt', 'r')
# input = sys.stdin.readline

N, M = map(lambda x: int(x), input().split())

password = {}

for i in range(N):
    site, pw = sys.stdin.readline().strip().split()
    password[site] = pw

for j in range(M):
    site = sys.stdin.readline().strip()
    print(password[site])

