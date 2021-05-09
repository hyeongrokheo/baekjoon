"""
problem tier : Silver 1 (solved_old.ac)
"""

import sys

def check(c):
    last_c = -99999999999
    count = 0
    for i in houses:
        if i-last_c >= c:
        # if last_c <= i:
            last_c = i
            count += 1
    if count >= C:
        return True
    else:
        return False

houses = []

N, C = map(lambda x: int(x), input().split())

for i in range(N):
    houses.append(int(sys.stdin.readline().strip()))

houses.sort()
# print(houses)

left, right = 0, max(houses)
while True:
    if left == right:
        break

    mid = (left + right + 1) // 2
    # print(left, right, mid)
    if check(mid):
        # print('true')
        left = mid
    else:
        # print('false')
        right = mid-1

print(left)
