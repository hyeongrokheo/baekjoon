"""
problem tier : Silver 4 (solved_old.ac)
"""

import sys
import math

N = int(input())
arr = []
count_arr = [0]*8001
sum_num = 0
min_num = 4000
max_num = -4000
for i in range(N):
    num = int(sys.stdin.readline())
    arr.append(num)
    count_arr[num+4000] += 1
    sum_num += num
    if max_num < num:
        max_num = num
    if min_num > num:
        min_num = num

arr.sort()

#산술평균
# print('산술')
if sum_num > 0:
    print(math.trunc(sum_num / N + 0.5))
else:
    print(math.floor(sum_num / N + 0.5))
#중앙값
print(arr[int((N-1)/2)])
#최빈값
maxcount = max(count_arr)
# print('maxcount :', maxcount)
# print(count_arr)
if count_arr.count(maxcount) == 1:
    print(count_arr.index(maxcount) - 4000)
else:
    print(count_arr.index(maxcount, count_arr.index(maxcount) + 1) - 4000)
#범위
print(max_num-min_num)