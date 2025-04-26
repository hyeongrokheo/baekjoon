"""
코딩테스트 연습 > 탐욕법(Greedy)
"""

def union_find_parent(union, v1):
    p = v1
    while p != union[p]:
        p = union[p]
    return p


def union_add(union, v1, v2):
    v1_parent = union_find_parent(union, union[v1])
    v2_parent = union_find_parent(union, union[v2])

    union[max(v1_parent, v2_parent)] = min(v1_parent, v2_parent)


def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    cost_sum = 0

    union = [i for i in range(n)]

    for cost in costs:
        a, b, c = cost

        if union_find_parent(union, a) != union_find_parent(union, b):
            union_add(union, a, b)
            cost_sum += c

    return cost_sum


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
