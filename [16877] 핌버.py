"""
problem tier : Platinum 3 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

grundy = [-1 for i in range(3*(10**6)+1)]
fibo_num = [1, 2]
while fibo_num[-1] < 3*(10**6)+1:
    fibo_num.append(fibo_num[-1] + fibo_num[-2])


def get_grundy(n):
    if grundy[n] >= 0:
        return grundy[n]
    else:
        candidate = list(map(lambda x: get_grundy(n-x), list(filter(lambda x: x<=n, fibo_num))))
        result = 0
        while result in candidate:
            result += 1
        grundy[n] = result
        return grundy[n]


N = int(input())
P = list(map(int, input().split()))
result = 0
for p in P:
    result ^= get_grundy(p)

if result == 0:
    print('cubelover')
else:
    print('koosaga')
