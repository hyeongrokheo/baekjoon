"""
problem tier : Gold 2 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N = int(input())

A, B, C = 0, 1, 1
for i in range((N % 1500000)):
    A, B, C = B, C, (B+C) % 1000000
print(A)
