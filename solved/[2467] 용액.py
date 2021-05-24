"""
problem tier : Gold 5 (solved.ac)
"""

N = int(input())

arr = list(map(lambda x: int(x), input().split()))

left, right = 0, N-1

min_num = 9999999999
min_left, min_right = None, None
while left < right:
    left_num = arr[left]
    right_num = arr[right]
    num = right_num + left_num
    if min_num > abs(num):
        min_num = abs(num)
        min_left, min_right = left, right
    if num < 0:
        left += 1
    elif num > 0:
        right -= 1
    else:
        break

print(arr[min_left], arr[min_right])
