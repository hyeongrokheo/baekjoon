"""
problem tier : Platinum 4 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def update(x, n, l, r):
    if l == r:
        seg_tree[n] += 1
    else:
        seg_tree[n] += 1
        mid = (l + r) // 2
        if x <= mid:
            update(x, n * 2, l, mid)
        else:
            update(x, n * 2 + 1, mid + 1, r)


def delete(x, n, l, r):
    if l == r:
        seg_tree[n] -= 1
        print(l)
        return seg_tree[n]
    else:
        seg_tree[n] -= 1
        mid = (l + r) // 2
        if x <= seg_tree[n*2]:
            delete(x, n * 2, l, mid)
        else:
            delete(x - seg_tree[n * 2], n * 2 + 1, mid + 1, r)

        return x - seg_tree[n]


tree_length = 2000000
N = int(input())
seg_tree = [0 for i in range(tree_length*4)]
for i in range(N):
    op, x = map(int, input().split())
    if op == 1:
        update(x, 1, 1, tree_length)
    else:
        delete(x, 1, 1, tree_length)
