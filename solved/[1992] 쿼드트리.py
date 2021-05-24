"""
problem tier : Silver 1 (solved.ac)
"""

N = int(input())
arr = []

for i in range(N):
    arr.append(list(map(lambda x: int(x), input())))
# print(arr)

def cut(x, y, N):
    black_num = 0
    for i in range(x, x+N):
        for j in range(y, y+N):
            black_num += arr[i][j]
    if black_num == 0:
        return '0'
    elif black_num == N**2:
        return '1'
    else:
        return '({}{}{}{})'.format(cut(x, y, N//2), cut(x, y+N//2, N//2),
                                  cut(x+N//2, y, N//2), cut(x+N//2, y+N//2, N//2))


# print(arr)
print(cut(0, 0, N))