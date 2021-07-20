"""
problem tier : Gold 2 (solved.ac)
"""

import sys
import heapq
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
Jewelry = []
for i in range(N):
    m, v = map(int, input().split())
    heapq.heappush(Jewelry, (m, v))

Bag = []
for i in range(K):
    b = int(input())
    heapq.heappush(Bag, (-b, b))

result = 0
Jewelry_available = []
while len(Bag) > 0:
    _, bag = heapq.heappop(Bag)
    while len(Jewelry) > 0 and Jewelry[0][0] <= bag:
        j = heapq.heappop(Jewelry)[1]
        heapq.heappush(Jewelry_available, (-j, j))

    if len(Jewelry_available) > 0:
        result += heapq.heappop(Jewelry_available)[1]

print(result)
