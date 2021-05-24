"""
problem tier : Bronze 2 (solved.ac)
"""

max_num = 1
max_index = 1
for i in range(9):
    num = int(input())
    if max_num < num:
        max_num = num
        max_index = i+1
print(max_num)
print(max_index)