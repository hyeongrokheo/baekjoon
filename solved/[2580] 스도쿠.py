"""
problem tier : Gold 4 (solved_old.ac)
pypy3
"""

board = []
for i in range(9):
    board.append(list(map(lambda x: int(x), input().split())))

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
                    # adj = list(set(adj))
                # if 0 in adj:
                #     adj.remove(0)
                avail = []
                for k in range(1, 10):
                    if k not in adj:
                        avail.append(k)
                # print('avail :', avail)
                if len(avail) == 0:
                    return
                for k in avail:
                    board[i][j] = k
                    Board()
                    board[i][j] = 0
                return
    for b in board:
        print(' '.join(map(str, b)))
    exit()

Board()