"""
problem tier : Silver 2 (solved.ac)
"""

from collections import deque
import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def solution():
    board_size = int(input())
    current_position = list(map(int, input().split()))
    target_position = list(map(int, input().split()))

    board = [[False for i in range(board_size)] for j in range(board_size)]

    queue = deque([(current_position, 0)])
    while len(queue) > 0:
        position, move = queue.popleft()
        if not (0 <= position[0] < board_size and 0 <= position[1] < board_size):
            continue
        if not board[position[0]][position[1]]:
            board[position[0]][position[1]] = True
        else:
            continue

        if position == target_position:
            return move
        else:
            for i in range(8):
                queue.append(([position[0]+dx[i], position[1]+dy[i]], move + 1))


T = int(input())
while T:
    print(solution())
    T -= 1
