"""
problem tier : Gold 4 (solved.ac)
"""

import heapq
import sys

cards = []
N = int(input())

for i in range(N):
    heapq.heappush(cards, int(sys.stdin.readline()))

result = 0

while len(cards) != 1:
    A = heapq.heappop(cards)
    B = heapq.heappop(cards)
    result += A+B
    heapq.heappush(cards, A+B)

print(result)
