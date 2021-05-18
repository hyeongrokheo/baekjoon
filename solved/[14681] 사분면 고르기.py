"""
problem tier : Bronze 4 (solved_old.ac)
"""

X = int(input())
Y = int(input())

if X > 0 and Y > 0:
    print(1)
elif X < 0 and Y > 0:
    print(2)
elif X < 0 and Y < 0:
    print(3)
else:
    print(4)