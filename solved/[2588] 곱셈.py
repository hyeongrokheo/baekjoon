"""
problem tier : Bronze 4 (solved_old.ac)
"""

int_A = int(input())
B = input()
int_B = int(B)
B = list(B)
B.reverse()
for b in B:
    print(int_A*int(b))
print(int_A * int_B)