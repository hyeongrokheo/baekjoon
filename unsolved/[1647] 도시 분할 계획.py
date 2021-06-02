"""
problem tier : Gold 4 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
roads = []
for i in range(M):
    A, B, C = map(int, input().split())
    roads.append((A, B, C))

roads.sort(key=lambda x: x[2])

cities = []
total_length = 0
max_length = 0
for road in roads:
    A, B, C = road
    A_city = -1
    B_city = -1
    for i in range(len(cities)):
        if A in cities[i]:
            A_city = i
        if B in cities[i]:
            B_city = i
        if A_city != -1 and B_city != -1:
            break
    if A_city != -1 and B_city != -1:
        if A_city == B_city:
            continue
        else:
            cities[A_city] = cities[A_city].union(cities[B_city])
            cities.remove(cities[B_city])
    elif A_city != -1 and B_city == -1:
        cities[A_city].add(B)
    elif A_city == -1 and B_city != -1:
        cities[B_city].add(A)
    else:
        cities.append(set([A, B]))
    total_length += C
    if max_length < C:
        max_length = C
    # print(cities)
# print(total_length)
# print(max_length)
print(total_length - max_length)
