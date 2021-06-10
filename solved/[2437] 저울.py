"""
problem tier : Gold 3 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
S = [0]

for num in arr:
    if len(S) == 0:
        S.append(num)
    else:
        S.append(S[-1] + num)

result = 1
for i in range(len(arr)):
    if S[i]+1 < arr[i]:
        result = S[i]+1
        break

if arr[0] == 1 and result == 1:
    result = S[-1] + 1

print(result)
