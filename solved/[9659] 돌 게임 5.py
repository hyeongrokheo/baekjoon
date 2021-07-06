"""
problem tier : Silver 2 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

N = int(input())

if N % 2 == 0:
    print('CY')
else:
    print('SK')

