"""
problem tier : Silver 3 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

N = int(input())

if N % 7 in [0, 2]:
    print('CY')
else:
    print('SK')
