"""
problem tier : Gold 1 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

N, M, K = map(int, input().split())

base = 1
exp = 0
while base < N:
    base *= 2
    exp += 1
exp += 1
seg_tree = [0] * (2**exp)


def st_update(X, V, N = 1, S = 1, E = N):
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


def st_query(L, R, N = 1, S = 1, E = N):
    if R < S or E < L:
        return 0
    elif L <= S and E <= R:
        return seg_tree[N]
    else:
        mid = (S + E) // 2
        return st_query(L, R, N * 2, S, mid) + st_query(L, R, N * 2 + 1, mid + 1, E)


for i in range(N):
    num = int(sys.stdin.readline())
    st_update(i+1, num)

for i in range(M + K):
    a, b, c = map(int, input().split())
    # print(a, b, c)
    if a == 1:
        st_update(b, c)
    elif a == 2:
        print(st_query(b, c))
