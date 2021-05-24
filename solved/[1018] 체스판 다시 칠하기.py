"""
problem tier : Silver 5 (solved.ac)
"""


def refillNum(board, i_base, j_base):
    count = 0
    for i in range(i_base, i_base+8):
        for j in range(j_base, j_base+8):
            # print(i, j)
            if (i+j) % 2 == 0 and board[i][j] == 'W':
                # print('C')
                count += 1
            elif (i+j) % 2 == 1 and board[i][j] == 'B':
                # print('C')
                count += 1

    if count > 32:
        count = 64 - count

    return count


N, M = map(lambda x: int(x), input().split())

board = []

for i in range(N):
    board.append(input())

best = 99
for i in range(N-7):
    for j in range(M-7):
        RN = refillNum(board, i, j)
        # exit()
        if best > RN:
            best = RN

print(best)
