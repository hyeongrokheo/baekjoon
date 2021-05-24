"""
problem tier : Platinum 5 (solved.ac)
"""

import sys
sys.setrecursionlimit(10**8)

def S(left, right):
    # print(left, right)
    # print(squares[left:right+1])
    if left >= right:
        return squares[right]
    elif right - left == 1:
        return max([squares[left], squares[right], min(squares[left], squares[right]) * 2])
    else:
        min_index = squares[left:right+1].index(min(squares[left:right+1])) + left
        # print('min index :', min_index)
        return max([S(left, min_index-1), S(min_index+1, right), squares[min_index] * (right-left+1)])

while True:
    inp = input()
    if inp == '0':
        break
    squares = list(map(lambda x: int(x), sys.stdin.readline().split()))

    n = squares[0]
    squares = squares[1:]

    # height_queue = []
    # for i in range(len(squares)):
    #     heapq.heappush(height_queue, (squares[i], i)

    print(S(0, n-1))

