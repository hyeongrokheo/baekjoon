"""
problem tier : Silver 2 (solved.ac)
"""

N = int(input())

arr = list(map(lambda x: int(x), input().split()))

sorted_uniq_arr = sorted(list(set(arr)))

map_table = {}

for i in range(len(sorted_uniq_arr)):
    map_table[sorted_uniq_arr[i]] = i

for num in arr:
    print(map_table[num], end=' ')

