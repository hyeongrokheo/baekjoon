"""
problem tier : Platinum 3 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N = int(input())
grundy = [None for i in range(N+1)]
grundy[0] = 0
grundy[1] = 0
grundy[2] = 1

def get_grundy(n):
    candidate = []
    if grundy[n-2] == None:
        get_grundy(n-2)
    candidate.append(grundy[n-2])
    for i in range(0, n-2):
        j = n-2-i
        if grundy[i] == None:
            get_grundy(i)
        if grundy[j] == None:
            get_grundy(j)
        candidate.append(grundy[i]^grundy[j])

    result = 0
    while result in candidate:
        result += 1
    grundy[n] = result
    return grundy[n]

if get_grundy(N) == 0:
    print(2)
else:
    print(1)
