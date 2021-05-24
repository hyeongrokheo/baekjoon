"""
problem tier : Silver 4 (solved.ac)
"""

N = int(input())
arr1 = list(map(lambda x: int(x), input().split()))
arr1.sort()

M = int(input())
arr2 = list(map(lambda x: int(x), input().split()))

def find(arr, num):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == num:
            return True
        if arr[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    # if left == right and arr[left] == num:
    #         return True
    return False


for num in arr2:
    if find(arr1, num):
        print(1)
    else:
        print(0)
