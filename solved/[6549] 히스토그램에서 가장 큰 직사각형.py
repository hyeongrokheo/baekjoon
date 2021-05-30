"""
problem tier : Platinum 5 (solved.ac)
"""

import sys
# sys.stdin = open('./../input.txt', 'r')
# input = sys.stdin.readline
sys.setrecursionlimit(101000)

INF = 2000000000

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
    global max_S
    if left == right:
        if max_S < squares[right]:
            max_S = squares[right]
        # return squares[right]
    elif left > right:
        None
        # return 0
    elif right - left == 1:
        s = max(squares[left], squares[right], min(squares[left], squares[right]) * 2)
        if max_S < s:
            max_S = s
        # return max(squares[left], squares[right], min(squares[left], squares[right]) * 2)
    else:
        mid = st_query(left+1, right+1, 1, 1, STN)
        mid = mid[1]
        func_stack.append([left, mid-1, STN])
        func_stack.append([mid+1, right, STN])
        # LS = S(left, mid-1, STN)
        # RS = S(mid+1, right, STN)
        # MS = (right-left+1) * squares[mid]
        s = (right - left + 1) * squares[mid]
        if max_S < s:
            max_S = s

        # return max(LS, RS, MS)

while True:
    global max_S
    inp = sys.stdin.readline().strip()
    if inp == '0':
        break
    squares = list(map(lambda x: int(x), inp.split()))

    n = squares[0]
    squares = squares[1:]

    base = 1
    exp = 0
    while base < n:
        base *= 2
        exp += 1

    seg_tree = [[INF, INF] for i in range(2 ** (exp+1))]

    for i in range(n):
        st_update(i+1, [squares[i], i], 1, 1, 2 ** exp)

    max_S = 0
    func_stack = [[0, n-1, 2**exp]]

    while len(func_stack) != 0:
        current_func = func_stack.pop()
        S(current_func[0], current_func[1], current_func[2])

    print(max_S)

