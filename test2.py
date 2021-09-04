from collections import defaultdict
from queue import Queue
import sys
input = sys.stdin.readline

def bfs(que, goal):
    route = []
    while(not que.empty()):
        parent = que.get()
        level = len(parent)
        for child in graph[parent[-1]]:
            if child == goal:
                route = parent + [child]
                que = Queue()
                break
            if height[child] < level:
                continue
            que.put(parent + [child])
            height[child] = level
    return route

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
s, e = map(int, input().split())
for node in range(n):
    graph[node].sort()

height = [n for _ in range(n+1)]
height[s] = 0
que = Queue()
que.put([s])
route = bfs(que, e)

ans = len(route)-1
height = [n if i not in route else 0 for i in range(n+1)]
height[s] = n
que = Queue()
que.put([e])
route = bfs(que, s)
print(ans+len(route)-1)