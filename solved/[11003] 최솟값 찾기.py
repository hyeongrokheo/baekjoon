"""
problem tier : Platinum 5 (solved.ac)
"""

import heapq
import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))

Q = []
R = []
for i in range(N):
    heapq.heappush(Q, arr[i])
    if len(Q) > L:
        heapq.heappush(R, arr[i-L])
    while len(R) > 0 and R[0] == Q[0]:
        heapq.heappop(R)
        heapq.heappop(Q)
    print(Q[0], end=' ')
