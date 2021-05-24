"""
problem tier : Gold 4 (solved.ac)
pypy3
"""

import sys
# sys.setrecursionlimit(10**8)

def Board():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                adj = []
                for k in range(9):
                    adj.append(board[i][k])
                    adj.append(board[k][j])
                    standard = [(i // 3) * 3, (j // 3) * 3]
                    for ii in range(standard[0], standard[0] + 3):
                        for jj in range(standard[1], standard[1] + 3):
                            adj.append(board[ii][jj])
                avail = []
                for k in range(1, 10):
                    if k not in adj:
                        avail.append(k)
                if len(avail) == 0:
                    return False
                for k in avail:
                    board[i][j] = k
                    if Board():
                        return True
                    board[i][j] = 0
                return False
    for b in board:
        print(''.join(map(str, b)))
    # print()
    return True

board = []
for i in range(9):
    board.append(list(map(lambda x: int(x), sys.stdin.readline().strip())))
# print(board)
Board()
