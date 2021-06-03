"""
problem tier : Gold 1 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N, Q = map(int, input().split())

base = 1
exp = 0
while base < N:
    base *= 2
    exp += 1
seg_tree = [0] * (2**(exp+1))


def st_update(X, V, N = 1, S = 1, E = 2 ** (exp)):
    if S == E:
        diff = V - seg_tree[N]
        seg_tree[N] = V
        return diff
    else:
        mid = (S + E) // 2
        if X <= mid:
            diff = st_update(X, V, 2 * N, S, mid)
            seg_tree[N] += diff
            return diff
        else:
            diff = st_update(X, V, 2 * N + 1, mid + 1, E)
            seg_tree[N] += diff
            return diff


def st_query(L, R, N = 1, S = 1, E = 2 ** (exp)):
    if R < S or E < L:
        return 0
    elif L <= S and E <= R:
        return seg_tree[N]
    else:
        mid = (S + E) // 2
        return st_query(L, R, N * 2, S, mid) + st_query(L, R, N * 2 + 1, mid + 1, E)


num = list(map(int, sys.stdin.readline().split()))
for i in range(len(num)):
    st_update(i+1, num[i])

for i in range(Q):
    x, y, a, b = map(int, input().split())
    if x > y:
        x, y = y, x
    print(st_query(x, y))
    st_update(a, b)
