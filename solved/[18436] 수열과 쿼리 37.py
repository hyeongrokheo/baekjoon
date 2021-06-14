"""
problem tier : Gold 1 (solved.ac)
"""

import sys
from copy import deepcopy
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

N = int(input())

seg_tree = [[0, 0] for i in range(N*4)]
#짝, 홀
def update(x, y, n, l, r):
    if l == r:
        old_leaf = deepcopy(seg_tree[n])
        new_leaf = [0, 0]
        new_leaf[y % 2] = 1
        seg_tree[n] = new_leaf
        dif_leaf = [new_leaf[0] - old_leaf[0], new_leaf[1] - old_leaf[1]]
        return dif_leaf
    else:
        mid = (l + r) // 2
        if x <= mid:
            dif = update(x, y, n * 2, l, mid)
        else:
            dif = update(x, y, n * 2 + 1, mid + 1, r)
        seg_tree[n][0] += dif[0]
        seg_tree[n][1] += dif[1]
        return dif


def query(s, e, n, l, r):
    if s <= l and r <= e:
        return seg_tree[n]
    elif r < s or e < l:
        return [0, 0]
    else:
        mid = (l + r) // 2
        left = query(s, e, n * 2, l, mid)
        right = query(s, e, n * 2 + 1, mid + 1, r)
        return [left[0] + right[0], left[1] + right[1]]


arr = list(map(int, input().split()))
for i in range(N):
    update(i+1, arr[i], 1, 1, N)

M = int(input())
for i in range(M):
    inp = list(map(int, input().split()))
    op = inp[0]
    if op == 1:
        i, x = inp[1], inp[2]
        update(i, x, 1, 1, N)
    elif op == 2:
        l, r = inp[1], inp[2]
        print(query(l, r, 1, 1, N)[0])
    else:
        l, r = inp[1], inp[2]
        print(query(l, r, 1, 1, N)[1])
