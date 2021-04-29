"""
problem tier : Silver 5 (solved_old.ac)
"""

import sys

N = int(input())

count_arr = [0]*10001
for i in range(N):
    count_arr[int(sys.stdin.readline())] += 1

for i in range(len(count_arr)):
    # i를 count_arr[i]번 출력
    for j in range(count_arr[i]):
        print(i)
