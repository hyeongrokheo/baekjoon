"""
problem tier : Gold 5 (solved.ac)
pypy3
"""


N, M = map(lambda x: int(x), input().split())
ancestor = [[False for j in range(M)] for i in range(N)]
stack = []

board = []
for i in range(N):
    board.append(list(map(lambda x: int(x), input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dx_2 = [2, -2, 0, 0]
dy_2 = [0, 0, 2, -2]

max_tetro = 0

def tetro(i, j, d):
    stack.append(board[i][j])
    ancestor[i][j] = True

    if d == 4:
        global max_tetro
        if max_tetro < sum(stack):
            max_tetro = sum(stack)
    else:
        for k in range(4):
            x = i+dx[k]
            y = j+dy[k]

            if 0 <= x < N and 0 <= y < M and not ancestor[x][y]:
                tetro(x, y, d+1)
        if d == 3:
            for k in range(4):
                x2 = i+dx[k]*2
                y2 = j+dy[k]*2

                if 0 <= x2 < N and 0 <= y2 < M and ancestor[x2][y2]:
                    x3 = i+dx[k]
                    y3 = j+dy[k]

                    for l in range(4):
                        x4 = x3+dx[l]
                        y4 = y3+dy[l]
                        if 0 <= x4 < N and 0 <= y4 < M and not ancestor[x4][y4]:
                            tetro(x4, y4, d+1)

    stack.pop()
    ancestor[i][j] = False


for i in range(N):
    for j in range(M):
        tetro(i, j, 1)

print(max_tetro)

