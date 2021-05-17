"""
problem tier : Gold 4 (solved_old.ac)
"""

R, C = map(lambda x: int(x), input().split())

board = []
for i in range(R):
    board.append(input())

stack = []
alphabet_ancient = [False for i in range(26)]
ancient = [[False for j in range(C)] for i in range(R)]
max_depth = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dp(depth):
    global max_depth
    position = stack[-1]
    x, y = position[0], position[1]
    if max_depth < depth:
        max_depth = depth

    for i in range(4):
        tx = x+dx[i]
        ty = y+dy[i]
        if 0 <= tx < R and 0 <= ty < C:
            talphabet = ord(board[tx][ty]) - ord('A')
            if not ancient[tx][ty] and not alphabet_ancient[talphabet]:
                stack.append([tx, ty])
                ancient[tx][ty] = True
                alphabet_ancient[talphabet] = True

                dp(depth+1)

                stack.pop()
                ancient[tx][ty] = False
                alphabet_ancient[talphabet] = False


stack.append([0, 0])
alphabet_ancient[ord(board[0][0]) - ord('A')] = True
dp(1)
print(max_depth)
