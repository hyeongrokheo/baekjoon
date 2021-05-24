"""
problem tier : Silver 5 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

S = set()

M = int(input())

for i in range(M):
    inp = sys.stdin.readline().strip().split()
    op = inp[0]
    if op in ['add', 'remove', 'check', 'toggle']:
        num = int(inp[1])

    if op == 'add':
        S.add(num)
    elif op == 'remove':
        if S.issuperset([num]):
            S.remove(num)
    elif op == 'check':
        if S.issuperset([num]):
            print(1)
        else:
            print(0)
    elif op == 'toggle':
        if S.issuperset([num]):
            S.remove(num)
        else:
            S.add(num)
    elif op == 'all':
        S = set([i for i in range(1, 21)])
    elif op == 'empty':
        S = set()
    else:
        print('Error')

