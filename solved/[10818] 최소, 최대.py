"""
problem tier : Bronze 3 (solved_old.ac)
"""

N = int(input())
num_arr = list(map(int, input().split(' ')))
min = 1000000
max = -1000000
for num in num_arr:
    if max <= num:
        max = num
    if min >= num:
        min = num
print("{} {}".format(min, max))