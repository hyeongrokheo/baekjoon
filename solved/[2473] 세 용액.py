"""
problem tier : Gold 4 (solved_old.ac)
"""

N = int(input())
arr = list(map(lambda x: int(x), input().split()))
arr.sort()
INF = 999999999999

def binary_search(n, l):
    left, right = l, N-1
    local_min_ae = INF
    min_n = None
    if left == right:
        min_n = arr[left]
    while left < right:
        mid = (left + right) // 2
        if local_min_ae > abs(arr[mid] + n):
            local_min_ae = abs(arr[mid] + n)
            min_n = arr[mid]

        if left + 1 == right:
            if abs(arr[left]+n) > abs(arr[right]+n):
                return arr[right]
            else:
                return arr[left]

        if arr[mid] + n == 0:
            return arr[mid]
        elif arr[mid] + n > 0:
            right = mid
        else:
            left = mid
    return min_n


min_ae = INF
min_list = None
for i in range(N):
    for j in range(i+1, N):
        two = arr[i]+arr[j]
        three = binary_search(two, j+1)
        if three and min_ae > abs(two + three):
            min_ae = abs(two+three)
            min_list = [arr[i], arr[j], three]

print(min_list[0], min_list[1], min_list[2])
