"""
problem tier : Silver 4 (solved_old.ac)
"""

N = int(input())

road = list(map(lambda x: int(x), input().split()))
oil = list(map(lambda x: int(x), input().split()))

cheapest = 1000000000
for i in range(len(oil)):
    if cheapest > oil[i]:
        cheapest = oil[i]
    else:
        oil[i] = cheapest

price = 0
for i in range(len(road)):
    price += road[i]*oil[i]

print(price)
