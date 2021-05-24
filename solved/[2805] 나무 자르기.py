"""
problem tier : Silver 3 (solved.ac)
"""

N, M = map(lambda x: int(x), input().split())
trees = list(map(lambda x: int(x), input().split()))


def get_wood(H):
    wood = 0
    for tree in trees:
        if tree > H:
            wood += tree-H
    return wood


left = 0
right = 1000000000
while left < right:
    mid = (left + right + 1) // 2
    # print(left, right, mid)
    wood = get_wood(mid)
    # print(wood)
    if M < wood:
        left = mid
    elif M > wood:
        right = mid-1
    else:
        left = mid

print(left)
