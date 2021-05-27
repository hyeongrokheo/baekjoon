"""
problem tier : Platinum 5 (solved.ac)
"""

import sys
sys.stdin = open('./../input.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

INF = 9999999999

def st_update(X, Y, N, S, E):
    if S == E:
        seg_tree[N] = Y
        return seg_tree[N]
    else:
        mid = (S + E) // 2
        if X <= mid:
            A = seg_tree[N]
            B = st_update(X, Y, N * 2, S, mid)
            if A[0] <= B[0]:
                seg_tree[N] = A
            else:
                seg_tree[N] = B
            return seg_tree[N]
        else:
            A = seg_tree[N]
            B = st_update(X, Y, N * 2 + 1, mid + 1, E)
            if A[0] <= B[0]:
                seg_tree[N] = A
            else:
                seg_tree[N] = B
            # seg_tree[N] = min(seg_tree[N], st_update(X, Y, N * 2 + 1, mid + 1, E))
            return seg_tree[N]


def st_query(L, R, N, S, E):
    if R < S or E < L:
        return [INF, INF]
    elif L <= S and E <= R:
        return seg_tree[N]
    else:
        mid = (S + E) // 2
        A = st_query(L, R, N * 2, S, mid)
        B = st_query(L, R, N * 2 + 1, mid+1, E)
        if A[0] <= B[0]:
            return A
        else:
            return B

def S(left, right, STN):
    if left == right:
        return squares[right]
    elif left > right:
        return 0
    else:
        mid = st_query(left, right, 1, 1, STN)[1]
        LS = S(left, mid-1, STN)
        RS = S(mid+1, right, STN)
        MS = (right-left+1) * squares[mid-1]
        return max(LS, RS, MS)


while True:
    global seg_tree

    inp = input()
    if inp == '0':
        break
    squares = list(map(lambda x: int(x), inp.split()))

    n = squares[0]
    squares = squares[1:]
    N = n * 4

    seg_tree = [[INF, INF] for i in range(N)]

    for i in range(n):
        st_update(i+1, [squares[i], i+1], 1, 1, n)
    print(S(0, n-1, n))

