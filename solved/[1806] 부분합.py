"""
problem tier : Gold 4 (solved_old.ac)
"""

INF = 100001

N, S = map(lambda x: int(x), input().split())
arr = list(map(lambda x: int(x), input().split()))

min_length = INF

left, right = 0, 0
s = arr[0]

while True:
    # print(s)
    if s >= S:
        if min_length > right - left + 1:
            min_length = right - left + 1
        if left == right:
            break
        s -= arr[left]
        left += 1
    else:
        right += 1
        if right == N:
            break
        s += arr[right]


if min_length == INF:
    print(0)
else:
    print(min_length)
