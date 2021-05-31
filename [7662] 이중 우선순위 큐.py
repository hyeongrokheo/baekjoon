"""
problem tier : Gold 5 (solved.ac)
"""

import heapq
import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

T = int(input())

while T:
    T -= 1

    Q_big = []
    Q_small = []
    big_poped = 0
    small_poped = 0
    K = int(input())
    for i in range(K):
        oper, num = input().split()
        num = int(num)
        if oper == 'I':
            heapq.heappush(Q_small, (num, num))
            heapq.heappush(Q_big, (-num, num))
        elif oper == 'D':
            if num == 1:
                if len(Q_big) > big_poped:
                    heapq.heappop(Q_big)
                if len(Q_small) > small_poped:
                    small_poped += 1
            elif num == -1:
                if len(Q_big) > big_poped:
                    big_poped += 1
                if len(Q_small) > small_poped:
                    heapq.heappop(Q_small)

    if len(Q_big) > big_poped:
        print(heapq.heappop(Q_big)[1], heapq.heappop(Q_small)[1])
    else:
        print('EMPTY')
