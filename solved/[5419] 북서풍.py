"""
problem tier : Platinum 4 (solved.ac)
"""


import sys
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline


def update(x, n, l, r):
    while True:
        seg_tree[n] += 1
        if l == r:
            break
        else:
            mid = (l + r) // 2
            if x <= mid:
                n = n * 2
                r = mid
            else:
                n = n * 2 + 1
                l = mid + 1


def query(s, e, n, l, r):
    S = [(s, e, n, l, r)]
    result = 0
    while len(S) > 0:
        s, e, n, l, r = S.pop()
        if e < l or r < s:
            continue
        elif s <= l and r <= e:
            result += seg_tree[n]
        else:
            mid = (l + r) // 2
            S.append((s, e, n*2, l, mid))
            S.append((s, e, n*2+1, mid+1, r))
    return result


T = int(input())

while T:
    T -= 1
    N = int(input())

    points = []
    for i in range(N):
        points.append(list(map(lambda x: int(x) + 10**9, sys.stdin.readline().split())))

    new_size = 1
    points.sort(key=lambda x: x[1])
    for i in range(len(points)):
        if i > 0 and points[i][1] != pre_y:
            new_size += 1
        pre_y = points[i][1]
        points[i][1] = new_size

    tree_size = 2
    while tree_size < new_size:
        tree_size *= 2
    seg_tree = [0 for i in range(tree_size * 2)]

    points.sort(key=lambda x: (x[0], -x[1]))
    count = 0
    for p in points:
        count += query(p[1], tree_size, 1, 1, tree_size)
        update(p[1], 1, 1, tree_size)

    print(count)
