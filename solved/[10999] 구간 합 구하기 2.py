"""
problem tier : Platinum 4 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N, M, K = map(int, input().split())

base = 1
exp = 0
while base < N:
    base *= 2
    exp += 1
exp += 1
seg_tree = [0] * (2**exp)
lazy_tree = [0] * (2**exp)

def st_update(L, R, V, N = 1, S = 1, E = 2**(exp-1)):
    if lazy_tree[N]:
        seg_tree[N] += lazy_tree[N] * (E-S+1)
        if S != E:
            lazy_tree[N * 2] += lazy_tree[N]
            lazy_tree[N * 2 + 1] += lazy_tree[N]
        lazy_tree[N] = 0
    if S == E:
        seg_tree[N] += V
    elif L <= S and E <= R:
        seg_tree[N] += V * (E-S+1)
        lazy_tree[2 * N] += V
        lazy_tree[2 * N + 1] += V
    else:
        mid = (S + E) // 2
        if L <= mid:
            st_update(L, R, V, 2 * N, S, mid)
        if mid < R:
            st_update(L, R, V, 2 * N + 1, mid + 1, E)
        seg_tree[N] += (min(R, E) - max(L, S) + 1) * V

def st_query(L, R, N = 1, S = 1, E = 2**(exp-1)):
    if lazy_tree[N]:
        seg_tree[N] += lazy_tree[N] * (E-S+1)
        if S != E:
            lazy_tree[N * 2] += lazy_tree[N]
            lazy_tree[N * 2 + 1] += lazy_tree[N]
        lazy_tree[N] = 0
    if R < S or E < L:
        return 0
    elif L <= S and E <= R:
        return seg_tree[N]
    else:
        mid = (S + E) // 2
        return st_query(L, R, N * 2, S, mid) + st_query(L, R, N * 2 + 1, mid + 1, E)

for i in range(N):
    num = int(sys.stdin.readline())
    st_update(i+1, i+1, num)
for i in range(M + K):
    inp = list(map(int, sys.stdin.readline().split()))
    a = inp[0]
    if a == 1:
        b, c, d = inp[1], inp[2], inp[3]
        st_update(b, c, d)
    elif a == 2:
        b, c = inp[1], inp[2]
        print(st_query(b, c))
