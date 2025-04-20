"""
코딩테스트 연습 > 완전탐색
"""


from copy import deepcopy


def solution(n, wires):
    max_diff = 1000
    for i in range(len(wires)):
        new_wires = deepcopy(wires)
        new_wires.pop(i)
        new_wires = [p for pair in new_wires for p in (pair, pair[::-1])]
        visited = bfs([1], [], new_wires)

        diff = abs(n - 2 * len(visited))
        if max_diff > diff:
            max_diff = diff

    return max_diff


def bfs(queue, visited, wires):
    if len(queue) == 0:
        return visited

    q = queue.pop(0)
    visited.append(q)
    queue.extend(list(filter(lambda x: x not in visited, map(lambda x: x[1], filter(lambda x: x[0] == q, wires)))))
    return bfs(queue, visited, wires)


print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
