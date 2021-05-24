"""
problem tier : Silver 1 (solved.ac)
"""

N = int(input())

arr = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(N-1):
    new_arr = [None] * 10
    new_arr[0] = arr[1]
    for j in range(1, 9):
        new_arr[j] = (arr[j-1] + arr[j+1]) % 1000000000
    new_arr[9] = arr[8]
    arr = new_arr
    # print(arr)
    # print(sum(arr))
print(sum(arr) % 1000000000)
