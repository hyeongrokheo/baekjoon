"""
problem tier : Silver 2 (solved_old.ac)
"""

def get_ADV(E, V):
    adjacent_vertex = []
    for edge in E:
        if edge[0] == V:
            adjacent_vertex.append(edge[1])
    adjacent_vertex.sort()
    return adjacent_vertex


def BFS(E, V):
    explored_vertex = [V]
    adjacent_vertex = get_ADV(E, V)
    while len(adjacent_vertex) > 0:
        target_vertex = adjacent_vertex[0]
        adjacent_vertex = adjacent_vertex[1:]
        if target_vertex not in explored_vertex:
            explored_vertex.append(target_vertex)
            adjacent_vertex.extend(get_ADV(E, target_vertex))
    return explored_vertex


def DFS(E, V, explored_vertex=None):
    if not explored_vertex:
        explored_vertex = [V]
    adjacent_vertex = get_ADV(E, V)
    for target_vertex in adjacent_vertex:
        if target_vertex not in explored_vertex:
            explored_vertex.append(target_vertex)
            explored_vertex = DFS(E, target_vertex, explored_vertex)
    return explored_vertex


def run():
    N, M, V = map(int, input().split())

    E = []
    for _ in range(M):
        P1, P2 = map(int, input().split())
        E.append([P1, P2])
        E.append([P2, P1])

    print(' '.join(map(str, DFS(E, V))))
    print(' '.join(map(str, BFS(E, V))))


run()