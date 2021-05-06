"""
problem tier : Silver 3 (solved_old.ac)
pypy3
"""

N, M, B = map(lambda x: int(x), input().split())

ground = []
for i in range(N):
    ground.extend(list(map(lambda x: int(x), input().split())))
# print(ground)
min_height = min(ground)
max_height = max(ground)
total_block = (sum(ground) + B)
if max_height > total_block // (N*M) :
    max_height = total_block // (N*M)

def get_time(height):
    time = 0
    for block in ground:
        if block > height:
            time += (block - height) * 2
        elif block < height:
            time += height - block
    return time

best_time = 999999999
best_height = None
for i in range(min_height, max_height+1):
    time = get_time(i)
    if best_time >= time:
        best_time = time
        best_height = i

print(best_time, best_height)
