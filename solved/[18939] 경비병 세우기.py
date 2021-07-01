"""
problem tier : Diamond 4 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

T = int(input())

while T:
    N, M, K = map(int, input().split())

    if 2 * K > max(N, M):
        print('Yuto')
    else:
        if (N * M - 2 * K * K) % 2 == 1:
            print('Yuto')
        else:
            print('Platina')

    T -= 1
