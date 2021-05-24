"""
problem tier : Silver 4 (solved.ac)
"""

hash_table = [0] * 20000001

N = int(input())
arr = list(map(lambda x: int(x), input().split()))
for i in arr:
    hash_table[i+10000000] += 1

M = int(input())
arr = list(map(lambda x: int(x), input().split()))
for i in arr:
    print(hash_table[i+10000000], end=' ')
