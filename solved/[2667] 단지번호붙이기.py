"""
problem tier : Silver 1 (solved.ac)
"""

N = int(input())

maps = []
for i in range(N):
    maps.append(list(map(lambda x: int(x), input())))

def get_adj_list(x, y):
    adj_list = []
    if x > 0 and maps[x-1][y] == 1:
        adj_list.append([x-1, y])
    if y > 0 and maps[x][y-1] == 1:
        adj_list.append([x, y-1])
    if x < N-1 and maps[x+1][y] == 1:
        adj_list.append([x+1, y])
    if y < N-1 and maps[x][y+1] == 1:
        adj_list.append([x, y+1])

    return adj_list

def group(x, y):
    group_count = 0
    if maps[x][y] == 1:
        group_count += 1
        maps[x][y] = 0
        adj_list = get_adj_list(x, y)
        for adj in adj_list:
            group_count += group(adj[0], adj[1])
    return group_count

count = 0
group_size_list = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            count += 1
            group_size_list.append(group(i, j))

print(count)
group_size_list.sort()
for group_size in group_size_list:
    print(group_size)