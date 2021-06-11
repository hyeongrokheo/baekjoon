"""
problem tier : Gold 5 (solved.ac)
"""

import heapq
import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

N = int(input())
Q = []

for i in range(N):
    inp = list(map(int, input().split()))
    for j in range(N):
        if len(Q) < N:
            heapq.heappush(Q, inp[j])
        else:
            if inp[j] > Q[0]:
                heapq.heappush(Q, inp[j])
                heapq.heappop(Q)

print(Q[0])
