"""
problem tier : Gold 4 (solved.ac)
"""

import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N = int(input())
length = [[] for i in range(N+1)]
for i in range(N-1):
    s, e, d = map(int, input().split())
    length[s].append([e, d])
    length[e].append([s, d])

visited = [False for i in range(N+1)]
far_point = None
max_length = 0

def DFS(s, l):
    global max_length, far_point
    leaf = True
    for next in length[s]:
        if not visited[next[0]]:
            leaf = False
            visited[next[0]] = True
            DFS(next[0], l+next[1])
            visited[next[0]] = False
    if leaf and max_length < l:
        far_point = s
        max_length = l

DFS(1, 0)
visited = [False for i in range(N+1)]
DFS(far_point, 0)

print(max_length)
