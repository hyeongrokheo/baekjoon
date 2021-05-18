"""
problem tier : Bronze 2 (solved_old.ac)
"""


num_arr = []
for i in range(10):
    num = int(input()) % 42
    num_arr.append(num)

print(len(list(set(num_arr))))