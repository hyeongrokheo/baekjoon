"""
코딩테스트 연습 > 힙
"""

import heapq


def solution(operations):
    max_heap = []
    min_heap = []

    for operation in operations:
        op_list = operation.split()
        operand = op_list[0]
        value = int(op_list[1])

        if operand == "I":
            heapq.heappush(max_heap, -value)
            heapq.heappush(min_heap, value)
        if operand == "D" and value == 1 and len(max_heap) > 0:
            v = heapq.heappop(max_heap)
            min_heap.remove(-v)
        if operand == "D" and value == -1 and len(min_heap) > 0:
            v = heapq.heappop(min_heap)
            max_heap.remove(-v)

    if len(max_heap) == 0 or len(min_heap) == 0:
        return [0, 0]
    if -max_heap[0] >= min_heap[0]:
        return [-max_heap[0], min_heap[0]]
    else:
        return [0, 0]


# print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I 10", "I 20", "D 1", "I 30", "I 40", "D -1", "D -1"]))
