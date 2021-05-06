"""
problem tier : Bronze 2 (solved_old.ac)
"""

r = 31
M = 1234567891
L = int(input())
word = input()

hashing = 0
for i in range(len(word)):
    hashing += (31**i)*(ord(word[i])-96)
    hashing %= 1234567891

print(hashing)
