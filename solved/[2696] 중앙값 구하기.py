"""
problem tier : Gold 2 (solved.ac)
"""

import heapq
import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

INF = 2 ** 32
T = int(input())

while T:
    T -= 1

    N = int(input())
    arr = []
    while N > 0:
        N -= 10
        arr.extend(list(map(int, input().split())))
    arr.reverse()

    left_Q, right_Q = [], []
    heapq.heappush(left_Q, (INF, -INF))
    heapq.heappush(right_Q, INF)
    mid = arr.pop()
    result = [mid]
    while len(arr) > 0:
        mids = [mid, arr.pop(), arr.pop(), heapq.heappop(left_Q)[1], heapq.heappop(right_Q)]
        mids.sort()
        heapq.heappush(left_Q, (-mids[0], mids[0]))
        heapq.heappush(left_Q, (-mids[1], mids[1]))
        mid = mids[2]
        heapq.heappush(right_Q, mids[3])
        heapq.heappush(right_Q, mids[4])
        result.append(mid)

    print(len(result))
    while len(result) > 0:
        if len(result) > 10:
            print(' '.join(map(str, result[:10])))
            result = result[10:]
        else:
            print(' '.join(map(str, result)))
            break