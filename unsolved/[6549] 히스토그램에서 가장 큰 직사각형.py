"""
problem tier : Platinum 5 (solved_old.ac)
"""

import heapq

def S(left, right):
    if left == right:
        return squares[left]
    elif right - left == 1:
        return max([squares[left], squares[right], min(squares[left], squares[right]) * 2])
    else:
        min(squares[left:right+1]) *
        # mid = (left + right) // 2
        # left_length = 0
        # right_length = 0
        # for i in range(mid-left):
        #     if squares[mid-i-1] >= squares[mid]:
        #         left_length += 1
        #     else:
        #         break
        # for i in range(right-mid):
        #     if squares[mid+i+1] >= squares[mid]:
        #         right_length += 1
        #     else:
        #         break
        # mid_S = squares[mid] * (left_length + right_length + 1)
        mid = min_height(left, right)
        mid_S = (right-left+1) * squares[mid]
        left_S = S(left, mid-1)
        right_S = S(mid+1, right)
        return max([mid_S, left_S, right_S])

while True:
    inp = input()
    if inp == '0':
        break
    squares = list(map(lambda x: int(x), inp.split()))

    n = squares[0]
    squares = squares[1:]

    height_queue = []
    for i in range(len(squares)):
        heapq.heappush(height_queue, (squares[i], i)

    print(S(0, n-1))




