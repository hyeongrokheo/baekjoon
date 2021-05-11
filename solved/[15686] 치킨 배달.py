"""
problem tier : Gold 5 (solved_old.ac)
"""

import sys
sys.setrecursionlimit(10**6)

N, M = map(lambda x: int(x), input().split())

maps = []
for i in range(N):
    maps.append(list(map(lambda x: int(x), input().split())))

house = []
chicken = []
count = 0
# print(maps)
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            house.append([i, j])
        elif maps[i][j] == 2:
            chicken.append([count, i, j])
            count += 1


selected_chicken = []
def calculate():
    dist_sum = 0
    for h in house:
        min_dist = 200
        for c in selected_chicken:
            # print(h, c)
            dist = abs(h[0]-c[1]) + abs(h[1]-c[2])
            if min_dist > dist:
                min_dist = dist
        # print(min_dist)
        dist_sum += min_dist
    return dist_sum

# print(chicken)
min_chicken_distance = 999999
def bfs():
    global min_chicken_distance
    # print(selected_chicken)
    if len(selected_chicken) == M:
        chicken_distance = calculate()
        if min_chicken_distance > chicken_distance:
            min_chicken_distance = chicken_distance
    else:
        if len(selected_chicken) == 0:
            for c in chicken:
                selected_chicken.append(c)
                bfs()
                selected_chicken.pop()
        else:
            for c in chicken[selected_chicken[-1][0]+1:]:
                selected_chicken.append(c)
                bfs()
                selected_chicken.pop()

bfs()
print(min_chicken_distance)
