"""
problem tier : Silver 3 (solved_old.ac)
"""

N = int(input())


a, b = 0, 1
for i in range(N):
    a, b = b, (a + b) % 15746
print(b)