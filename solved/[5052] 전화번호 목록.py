"""
problem tier : Gold 4 (solved_old.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

T = int(input())

while T:
    T -= 1
    N = int(input())

    numbers = []
    for i in range(N):
        numbers.append(sys.stdin.readline().strip())
    numbers.sort()

    result = True
    for i in range(N-1):
        if numbers[i+1].startswith(numbers[i]):
            result = False
    if result:
        print('YES')
    else:
        print('NO')
