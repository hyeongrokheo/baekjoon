"""
problem tier : Silver 4 (solved.ac)
"""

n = int(input())
arr = list(map(lambda x: int(x), input().split()))
x = int(input())

arr.sort()

count = 0
left, right = 0, n-1
while True:
    if left >= right:
        break
    else:
        if arr[left] + arr[right] == x:
            count += 1
            left += 1
            right -= 1
        elif arr[left] + arr[right] > x:
            right -= 1
        else:
            left += 1

print(count)
