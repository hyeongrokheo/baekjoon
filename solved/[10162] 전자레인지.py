"""
problem tier : Bronze 4 (solved.ac)
"""

# import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

T = int(input())

A = T // 300
B = (T % 300) // 60
C = (T % 60) // 10

if T % 10 == 0:
    print(A, B, C)
else:
    print(-1)
