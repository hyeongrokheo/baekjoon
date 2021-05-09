"""
problem tier : Gold 5 (solved_old.ac)
"""

N, M = map(lambda x: int(x), input().split())

labs = []
for i in range(N):
    labs.append(list(map(lambda x: int(x), input().split())))

spread()
for l in labs:
    print(l)
