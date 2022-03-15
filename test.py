"""
problem tier : Silver 3 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline


stack = []

def bt():
    if len(stack) == N:
        print(' '.join(map(str, stack)))
        return
    for i in range(1, N+1):
        if i not in stack:
            stack.append(i)
            bt()
            stack.pop()


def solution():
    global N
    N = int(input())
    bt()


solution()
