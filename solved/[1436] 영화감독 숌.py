"""
problem tier : Silver 5 (solved_old.ac)
"""


N = int(input())

num = 0

while N:
    if str(num).find('666') != -1:
        N -= 1
    num += 1

num -= 1
print(num)
