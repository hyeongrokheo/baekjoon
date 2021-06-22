"""
problem tier : Platinum 3 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def update(s, e, n, l, r):
    if lazy_tree[n] and lazy_tree[n] % 2 == 1:
        seg_tree[n] = r - l + 1 - seg_tree[n]
        if l != r:
            lazy_tree[n*2] += 1
            lazy_tree[n*2+1] += 1
        lazy_tree[n] = 0

    if s <= l and r <= e:
        ori = seg_tree[n]
        seg_tree[n] = r - l + 1 - seg_tree[n]
        dif = seg_tree[n] - ori
        if l != r:
            lazy_tree[n*2] += 1
            lazy_tree[n*2+1] += 1
        return dif
    elif r < s or e < l:
        return 0
    else:
        mid = (l+r)//2
        dif = update(s, e, n*2, l, mid) + update(s, e, n*2+1, mid+1, r)
        seg_tree[n] += dif
        return dif


def query(s, e, n, l, r):
    if lazy_tree[n] and lazy_tree[n] % 2 == 1:
        seg_tree[n] = r - l + 1 - seg_tree[n]
        if l != r:
            lazy_tree[n*2] += 1
            lazy_tree[n*2+1] += 1
        lazy_tree[n] = 0

    if s <= l and r <= e:
        return seg_tree[n]
    elif r < s or e < l:
        return 0
    else:
        mid = (l+r)//2
        return query(s, e, n*2, l, mid) + query(s, e, n*2+1, mid+1, r)



N, M = map(int, input().split())

seg_tree = [0 for i in range(N * 4)]
lazy_tree = [0 for i in range(N * 4)]

for i in range(M):
    o, a, b = map(int, input().split())
    if o == 0:
        update(a, b, 1, 1, N)
    else:
        print(query(a, b, 1, 1, N))
