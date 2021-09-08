"""
코딩테스트 연습 > 2019 KAKAO BLIND RECRUITMENT > 실패율
"""


def update(seg_tree, x, n, l, r):
    if l == r:
        seg_tree[n] += 1
    else:
        seg_tree[n] += 1
        mid = (l+r)//2
        if x <= mid:
            update(seg_tree, x, n*2, l, mid)
        else:
            update(seg_tree, x, n*2+1, mid+1, r)


def query(seg_tree, s, e, n, l, r):
    mid = (l + r) // 2
    if r < s or e < l:
        return 0
    elif s <= l and r <= e:
        return seg_tree[n]
    else:
        return query(seg_tree, s, e, n*2, l, mid) + query(seg_tree, s, e, n*2+1, mid+1, r)


def solution(N, stages):
    N += 1
    tree_len = N*4
    seg_tree = [0 for i in range(tree_len)]
    for stage in stages:
        update(seg_tree, stage, 1, 1, N)

    result = []
    stage_list = []
    for i in range(1, N):
        arrived = query(seg_tree, i, i, 1, 1, N)
        failed = query(seg_tree, i, N, 1, 1, N)

        if failed == 0:
            rate = 0
        else:
            rate = arrived / failed
        stage_list.append([rate, i])
    stage_list.sort(key=lambda x: -x[0])
    stage_list = list(map(lambda x: x[1], stage_list))
    return stage_list

print(solution(5, [1]))
