"""
problem tier : Gold 4 (solved_old.ac)
"""

N = int(input())
arr = list(map(lambda x: int(x), input().split()))
arr.sort()
print(arr)
INF = 9999999999

def binary_search(n, l): # 가장 0에 가까운 값 반환
    left, right = l, N-1
    local_min_ae = INF
    # print(left, right)
    min_n = None
    while left < right:
        mid = (left + right) // 2
        print(left, right, mid)
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

# print(binary_search(60, 0))
# exit()


min_ae = INF
min_list = None
for i in range(N):
    for j in range(i+1, N):
        if i == 0 and j == 2:
            print('this')
        two = arr[i]+arr[j]
        print(two)
        three = binary_search(two, j+1)
        if three and min_ae > two + three:
            min_list = [arr[i], arr[j], three]

print(min_list)
