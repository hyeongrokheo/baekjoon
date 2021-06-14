"""
problem tier : Silver 5 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

M = int(input())
XOR = 0
S = 0
for i in range(M):
    Q = list(map(int, input().split()))
    oper = Q[0]
    if oper == 1:
        x = Q[1]
        XOR = XOR ^ x
        S = S + x
    elif oper == 2:
        x = Q[1]
        XOR = XOR ^ x
        S = S - x
    elif oper == 3:
        print(S)
    elif oper == 4:
        print(XOR)

