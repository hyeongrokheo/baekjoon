"""
problem tier : Platinum 5 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

index_map = {}
for i in range(N):
    index_map[arr1[i]] = i+1

seg_tree = [0 for i in range(N * 4)]

def update(x, n, l, r):
    if l == r:
        seg_tree[n] += 1
    else:
        mid = (l + r) // 2
        if x <= mid:
            update(x, n * 2, l, mid)
        else:
            update(x, n * 2 + 1, mid + 1, r)
        seg_tree[n] += 1

def query(s, e, n, l, r):
    # print(s, e, n, l, r)
    if s <= l and r <= e:
        return seg_tree[n]
    elif r < s or e < l:
        return 0
    else:
        mid = (l + r) // 2
        return query(s, e, n * 2, l, mid) + query(s, e, n * 2 + 1, mid + 1, r)

cross = 0
for num in arr2:
    update(index_map[num], 1, 1, N)
    cross += query(index_map[num]+1, N, 1, 1, N)

print(cross)

