"""
problem tier : Gold 4 (solved.ac)
"""

import sys
input = sys.stdin.readline

K = int(input())

while K:
    K -= 1
    V, E = map(int, input().split())
    length = {}
    for i in range(E):
        s, e = map(lambda x: int(x)-1, input().split())
        if s not in length.keys():
            length[s] = []
        if e not in length.keys():
            length[e] = []
        length[s].append(e)
        length[e].append(s)

    colors = [0 for i in range(V)]
    group_count = 0
    for i in range(V):
        if colors[i] == 0:
            group_count += 1
            stack = [(i, 1)]
            duplicate_color = False
            while len(stack) > 0:
                v, c = stack.pop()
                if colors[v] == 0:
                    colors[v] = c
                    if v in length.keys():
                        for next in length[v]:
                            stack.append((next, c % 2 + 1))
                elif colors[v] == c:
                    None
                else:
                    duplicate_color = True
                    break
            if duplicate_color:
                break

    if duplicate_color:
        print('NO')
    else:
        print('YES')
