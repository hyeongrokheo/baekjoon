"""
problem tier : Bronze 1 (solved_old.ac)
"""


import math

inp = list(map(int, input().split(' ')))
A = inp[0]
B = inp[1]
V = inp[2]

step_size = A-B
just_before_end_target = V-A
step = math.ceil(just_before_end_target / step_size)
print(step+1)