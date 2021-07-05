"""
problem tier : Platinum 4 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def update(s, e, y, n, l, r):
    global seg_tree, lazy_tree
    if lazy_tree[n]:
        if (r - l + 1) % 2 == 1:
            seg_tree[n] = seg_tree[n] ^ lazy_tree[n]
        if l != r:
            lazy_tree[n*2] ^= lazy_tree[n]
            lazy_tree[n*2+1] ^= lazy_tree[n]
        lazy_tree[n] = 0

    if s <= l and r <= e:
        if (r-l+1) % 2 == 1:
            seg_tree[n] ^= y
        if l != r:
            lazy_tree[n*2] ^= y
            lazy_tree[n*2+1] ^= y
        return r-l+1
    elif r < s or e < l:
        return 0
    else:
        mid = (l+r)//2
        upd = update(s, e, y, n*2, l, mid) + update(s, e, y, n*2+1, mid+1, r)
        if upd % 2 == 1:
            seg_tree[n] = seg_tree[n] ^ y
        return upd


def query(s, e, n, l, r):
    global seg_tree, lazy_tree
    if lazy_tree[n]:
        if (r-l+1) % 2 == 1:
            seg_tree[n] = seg_tree[n] ^ lazy_tree[n]
        if l != r:
            lazy_tree[n*2] ^= lazy_tree[n]
            lazy_tree[n*2+1] ^= lazy_tree[n]
        lazy_tree[n] = 0

    if s <= l and r <= e:
        return seg_tree[n]
    elif r < s or e < l:
        return 0
    else:
        mid = (l+r)//2
        return query(s, e, n*2, l, mid) ^ query(s, e, n*2+1, mid+1, r)


N = int(input())
arr = list(map(int, input().split()))

seg_tree = [0 for i in range(N*4)]
lazy_tree = [0 for i in range(N*4)]

for i in range(N):
    update(i+1, i+1, arr[i], 1, 1, N)

M = int(input())
for i in range(M):
    inp = list(map(int, input().split()))
    o = inp[0]
    if o == 1:
        i, j, k = inp[1], inp[2], inp[3]
        update(i+1, j+1, k, 1, 1, N)
    else:
        i = inp[1]
        print(query(i+1, i+1, 1, 1, N))
