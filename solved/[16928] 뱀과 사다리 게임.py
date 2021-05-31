"""
problem tier : Silver 1 (solved.ac)
"""

from collections import deque
import sys
input = sys.stdin.readline

INF = 99999
memo = [None for i in range(101)]
board = [None for i in range(101)]

N, M = map(int, input().split())

for i in range(N + M):
    x, y = map(int, input().split())
    board[x] = y

queue = deque()
queue.append((0, 1))
memo[1] = 0

while len(queue) > 0:
    dice, position = queue.popleft()

    for i in range(1, 7):
        if position + i > 100:
            continue
        if board[position + i]:
            if not memo[board[position + i]]:
                memo[board[position + i]] = dice + 1
                queue.append((dice + 1, board[position + i]))
        else:
            if not memo[position + i]:
                memo[position + i] = dice + 1
                queue.append((dice + 1, position + i))

print(memo[100])
