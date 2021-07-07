"""
problem tier : Platinum 4 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N = int(input())
memo = [0, 1, 1, 1, 2, 2]
memo.extend([None for i in range(1995)])

def grundy(n):
    if n < 0:
        return 0
    if memo[n] != None:
        return memo[n]
    else:
        mex = []
        mex.append(grundy(n - 3))
        mex.append(grundy(n - 4))
        mex.append(grundy(n - 5))
        for i in range(1, (n - 3) // 2):
            mex.append(grundy(i) ^ grundy(n - 5 - i))
        grundy_num = 0
        while grundy_num in mex:
            grundy_num += 1

        memo[n] = grundy_num
        return memo[n]


if grundy(N) == 0:
    print(2)
else:
    print(1)

