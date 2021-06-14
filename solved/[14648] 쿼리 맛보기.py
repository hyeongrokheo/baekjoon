"""
problem tier : Bronze 1 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

N, Q = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(Q):
    q = list(map(int, input().split()))

    if q[0] == 1:
        a, b = q[1]-1, q[2]-1
        print(sum(arr[a:b+1]))
        arr[a], arr[b] = arr[b], arr[a]
    else:
        a, b, c, d = q[1]-1, q[2]-1, q[3]-1, q[4]-1
        print(sum(arr[a:b+1]) - sum(arr[c:d+1]))

