"""
problem tier : Bronze 4 (solved_old.ac)
"""


year = int(input())
if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print(1)
        exit()
print(0)
exit()