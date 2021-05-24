"""
problem tier : Gold 3 (solved.ac)
"""

N = int(input())
k = int(input())


def get_real_devider(n, d):
    if n%d == 0:
        return n//d - 1
    else:
        return n//d

def in_index(num):
    count = 0
    for i in range(1, min(num, N+1)):
        count += min(get_real_devider(num, i), N)
    return count

left, right = 1, N**2

while True:
    if left == right:
        break
    mid = (left + right + 1) // 2
    count = in_index(mid)
    if count >= k:
        right = mid-1
    elif count < k:
        left = mid
print(right)
