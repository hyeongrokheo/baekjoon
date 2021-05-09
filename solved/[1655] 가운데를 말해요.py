"""
problem tier : Gold 2 (solved_old.ac)
"""

import sys, heapq

N = int(input())

left_queue = []  # 큰 수 먼저 나와야 됨
right_queue = []  # 작은 수 먼저 나와야 됨
mid = 0

for i in range(N):
    num = int(sys.stdin.readline())

    if i == 0:
        mid = num
    elif i == 1:
        if mid > num:
            heapq.heappush(right_queue, mid)
            mid = num
        elif mid <= num:
            heapq.heappush(right_queue, num)
    elif i == 2:
        if num <= mid:
            heapq.heappush(left_queue, (-num, num))
        elif num >= right_queue[0]:
            heapq.heappush(left_queue, (-mid, mid))
            mid = heapq.heappop(right_queue)
            heapq.heappush(right_queue, num)
        else:
            heapq.heappush(left_queue, (-mid, mid))
            mid = num
    else:
        left = heapq.heappop(left_queue)
        right = heapq.heappop(right_queue)

        midarr = [left[1], right, mid, num]
        midarr.sort()

        if len(left_queue) == len(right_queue):
            heapq.heappush(left_queue, (-midarr[0], midarr[0]))
            mid = midarr[1]
            heapq.heappush(right_queue, midarr[2])
            heapq.heappush(right_queue, midarr[3])
        else:
            heapq.heappush(left_queue, (-midarr[0], midarr[0]))
            heapq.heappush(left_queue, (-midarr[1], midarr[1]))
            mid = midarr[2]
            heapq.heappush(right_queue, midarr[3])

    print(mid)
