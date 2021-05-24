"""
problem tier : Silver 2 (solved.ac)
"""

N = int(input())

arr = []
for i in range(N):
    start, end = map(lambda x: int(x), input().split())
    arr.append([start, end])
arr.sort(key=lambda x: (x[1], x[0]))

current_time = 0
count = 0
for i in arr:
    # print(i[0], i[1], current_time)
    if current_time > i[0]:
        continue
    if current_time <= i[1]:
        # print(i[0], current_time, i[1])
        # print(i[0], i[1])
        current_time = i[1]
        count += 1

print(count)