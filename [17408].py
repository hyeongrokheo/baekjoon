"""
problem tier : Platinum 3 (solved.ac)
"""

import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline


def update(x, y, n, l, r):
    if x == r:
        seg_tree[n][0] = y
    else:
        mid = (l + r) // 2
        if x <= mid:
            update(x, y, n * 2, l, mid)
        else:
            update(x, y, n * 2 + 1, mid + 1, r)
        seg_tree[n].append(y)
        seg_tree[n].sort(reverse=True)
        seg_tree[n].pop()


def query(s, e, n, l, r):
    print(s, e, n, l, r)
    if s <= l and r <= e:
        return seg_tree[n]
    elif r < s or e < l:
        return [0, 0]
    else:
        result = seg_tree[n]
        mid = (l + r) // 2
        result.extend(query(s, e, n * 2, l, mid))
        result.extend(query(s, e, n * 2 + 1, mid + 1, r))
        result.sort(reverse=True)
        result.pop()
        result.pop()
        result.pop()
        result.pop()
        return result


N = int(input())
arr = list(map(int, input().split()))
seg_tree = [[0, 0] for i in range(N*4)]
for i in range(N):
    update(i + 1, arr[i], 1, 1, N)
    print(seg_tree)
# print(seg_tree)
M = int(input())
print(query(1, 5, 1, 1, N))
# for i in range(1):
#     inp = list(map(int, input().split()))
#     op = inp[0]
#     if op == 1:
#         i, v = inp[1], inp[2]
#         update(i, v, 1, 1, N)
#     else:
#         l, r = inp[1], inp[2]
#         print(query(l, r, 1, 1, N))

