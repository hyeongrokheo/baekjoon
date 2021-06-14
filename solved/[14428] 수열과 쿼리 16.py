"""
problem tier : Gold 1 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def update(x, y, n, l, r):
    if x < l or x > r:
        None
    elif l == r:
        seg_tree[n] = (x, y)
    elif l <= x <= r:
        mid = (l+r)//2
        seg_tree[n] = min(update(x, y, n*2, l, mid), update(x, y, n*2+1, mid+1, r), key=lambda x: x[1])
    return seg_tree[n]

def query(s, e, n, l, r):
    if s <= l and r <= e:
        return seg_tree[n]
    elif r < s or e < l:
        return (INF, INF)
    else:
        mid = (l+r)//2
        return min(query(s, e, n*2, l, mid), query(s, e, n*2+1, mid+1, r), key=lambda x: (x[1], x[0]))


INF = 9999999999
N = int(input())
tree_size = 2
while tree_size < N:
    tree_size *= 2
seg_tree = [[INF, INF] for i in range(tree_size * 2)]
arr = list(map(int, input().split()))
for i in range(N):
    update(i+1, arr[i], 1, 1, tree_size)
M = int(input())

for i in range(M):
    inp = list(map(int, input().split()))
    if inp[0] == 1:
        i, j = inp[1], inp[2]
        update(i, j, 1, 1, tree_size)
    else:
        i, j = inp[1], inp[2]
        print(query(i, j, 1, 1, tree_size)[0])
