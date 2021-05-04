"""
problem tier : Silver 3 (solved_old.ac)
"""

N = int(input())
arr = []

for i in range(N):
    arr.append(list(map(lambda x: int(x), input().split())))


def cut(x, y, N):
    blue_num = 0
    for i in range(x, x+N):
        for j in range(y, y+N):
            blue_num += arr[i][j]
    if blue_num == 0:
        return 1, 0
    elif blue_num == N**2:
        return [0, 1]
    else:
        w = [None]*4
        b = [None]*4

        w[0], b[0] = cut(x, y, N//2)
        w[1], b[1] = cut(x+N//2, y, N//2)
        w[2], b[2] = cut(x, y+N//2, N//2)
        w[3], b[3] = cut(x+N//2, y+N//2, N//2)

        return sum(w), sum(b)

# print(arr)
w, b = cut(0, 0, N)
print(w, b)