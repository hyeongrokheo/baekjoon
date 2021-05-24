"""
problem tier : Silver 1 (solved.ac)
"""

N = int(input())
star_arr = [[False for col in range(N)] for row in range(N)]

def star(x, y, N):
    flag = int(N/3)
    if N == 3:
        star_arr[x][y] = True
        star_arr[x + 1][y] = True
        star_arr[x + 2][y] = True
        star_arr[x][y + 1] = True
        star_arr[x + 2][y + 1] = True
        star_arr[x][y + 2] = True
        star_arr[x + 1][y + 2] = True
        star_arr[x + 2][y + 2] = True
    else:
        star(x, y, flag)
        star(x + flag, y, flag)
        star(x + flag * 2, y, flag)
        star(x, y + flag, flag)
        star(x + flag * 2, y + flag, flag)
        star(x, y + flag * 2, flag)
        star(x + flag, y + flag * 2, flag)
        star(x + flag * 2, y + flag * 2, flag)

star(0, 0, N)

for i in star_arr:
    for j in i:
        if j:
            print('*', end='')
        else:
            print(' ', end='')
    print()