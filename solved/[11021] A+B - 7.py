"""
problem tier : Bronze 3 (solved.ac)
"""

T = int(input())
for i in range(T):
    inp = list(map(int, input().split(' ')))
    A = inp[0]
    B = inp[1]
    print('Case #{}: {}'.format(i+1, A+B))