"""
problem tier : Silver 1 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N = int(input())

if N % 7 in [1, 3]:
    print('CY')
else:
    print('SK')
