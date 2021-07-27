"""
problem tier : Silver 4 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())

    if N == 1:
        return 1
    elif N == 2:
        if M < 7:
            return (M+1)//2
        else:
            return 4
    else:
        if M <= 4:
            return M
        elif M <= 6:
            return 4
        else:
            return M-2


print(solution())
# while True:
#     print(solution())
