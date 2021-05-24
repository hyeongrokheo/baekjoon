
T = int(input())


def search(cell_count, wire_count, x, y, drop_core):
    global max_core, min_length
    if max_core < cell_count:
        max_core = cell_count
        min_length = wire_count
    elif max_core == cell_count:
        if min_length > wire_count:
            min_length = wire_count

    if max_core > total_core - drop_core:
        return
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(N):
        if i < x:
            continue
        for j in range(N):
            if i == x and j <= y:
                continue


            else:
                if cell[i][j] == 1:
                    if i == 0 or i == N - 1 or j == 0 or j == N - 1:
                        search(cell_count + 1, wire_count, i, j, drop_core)
                    else:
                        for k in range(4):
                            c = 1
                            avail = True
                            while 0 <= i + dx[k] * c < N and 0 <= j + dy[k] * c < N:
                                if cell[i + dx[k] * c][j + dy[k] * c] >= 1:
                                    avail = False
                                    break
                                c += 1
                            if avail:
                                c = 1
                                wc = 0
                                while 0 <= i + dx[k] * c < N and 0 <= j + dy[k] * c < N:
                                    cell[i + dx[k] * c][j + dy[k] * c] = 2
                                    c += 1
                                    wc += 1
                                search(cell_count + 1, wire_count + wc, i, j, drop_core)
                                c = 1
                                while 0 <= i + dx[k] * c < N and 0 <= j + dy[k] * c < N:
                                    cell[i + dx[k] * c][j + dy[k] * c] = 0
                                    c += 1
                        search(cell_count, wire_count, i, j, drop_core + 1)

for t in range(T):
    N = int(input())

    global cell, max_core, min_length
    cell = []
    for i in range(N):
        cell.append(list(map(int, input().split())))

    total_core = 0
    for i in range(N):
        for j in range(N):
            if cell[i][j] == 1:
                total_core += 1
    max_core = 0
    min_length = 99999

    search(0, 0, -1, -1, 0)

    print('#{} {}'.format(t+1, min_length))
