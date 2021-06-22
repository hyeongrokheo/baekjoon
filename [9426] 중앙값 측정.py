"""
problem tier : Platinum 5 (solved.ac)
"""

from collections import deque
import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

def update(x, y, n, l, r):
    if l == r:
        seg_tree[n] += y
    else:
        seg_tree[n] += y
        mid = (l+r)//2
        if x <= mid:
            update(x, y, n*2, l, mid)
        else:
            update(x, y, n*2+1, mid+1, r)

def find_mid(lc, rc, n, l, r):
    # print(lc, rc, n, l, r)
    if l == r:
        # return seg_tree[n]
        return l
    else:
        mid = (l+r)//2
        if lc + seg_tree[2*n] > rc + seg_tree[2*n+1]:
            return find_mid(lc, rc+seg_tree[2*n+1], n*2, l, mid)
        else:
            return find_mid(lc+seg_tree[2*n], rc, n*2+1, mid+1, r)


N, K = map(int, input().split())
tree_size = 65536
seg_tree = [0 for i in range(tree_size*2)]

Q = deque()
result = 0
for i in range(N):
    new_T = int(input())+1
    update(new_T, 1, 1, 1, tree_size)
    Q.append(new_T)

    if len(Q) > K:
        update(Q.popleft(), -1, 1, 1, tree_size)
    # print(seg_tree)
    if len(Q) == K:
        # print(find_mid(0, 0, 1, 1, tree_size))
        result += find_mid(0, 0, 1, 1, tree_size) - 1

print(result)





