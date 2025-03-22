"""
코딩테스트 연습 > 힙
"""

import heapq

def solution(scoville, K):
    hq = []

    for s in scoville:
        heapq.heappush(hq, s)

    count = 0
    while len(hq) >= 2:
        s1 = heapq.heappop(hq)
        if s1 >= K:
            break
        s2 = heapq.heappop(hq)

        new_s = s1 + s2*2
        heapq.heappush(hq, new_s)
        count += 1

    if heapq.heappop(hq) < K:
        return -1
    else:
        return count
