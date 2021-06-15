"""
problem tier : Platinum 3 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def update(x, y, n, l, r):
    if x < l or x > r:
        return seg_tree[n]
    elif l == r:
        seg_tree[n][0] = y
        return seg_tree[n]
    else:
        mid = (l + r) // 2
        result = []
        result.extend(update(x, y, n * 2, l, mid))
        result.extend(update(x, y, n * 2 + 1, mid + 1, r))
        result.sort(reverse=True)
        result.pop()
        result.pop()
        seg_tree[n] = result
        return seg_tree[n]


def query(s, e, n, l, r):
    if s <= l and r <= e:
        return seg_tree[n]
    elif r < s or e < l:
        return [0, 0]
    else:
        result = []
        mid = (l + r) // 2
        result.extend(query(s, e, n * 2, l, mid))
        result.extend(query(s, e, n * 2 + 1, mid + 1, r))
        result.sort(reverse=True)
        result.pop()
        result.pop()
        return result


N = int(input())
arr = list(map(int, input().split()))
seg_tree = [[0, 0] for i in range(N*4)]
for i in range(N):
    update(i + 1, arr[i], 1, 1, N)
M = int(input())
for i in range(M):
    inp = list(map(int, input().split()))
    op = inp[0]
    if op == 1:
        i, v = inp[1], inp[2]
        update(i, v, 1, 1, N)
    else:
        l, r = inp[1], inp[2]
        print(sum(query(l, r, 1, 1, N)))

