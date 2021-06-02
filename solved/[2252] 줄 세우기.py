"""
problem tier : Gold 2 (solved.ac)
"""

from collections import deque
import sys
input = sys.stdin.readline

INF = 99999
N, M = map(int, input().split())


student = [[0, []] for i in range(N+1)]
for i in range(M):
    s, e = map(int, input().split())
    student[e][0] += 1
    student[s][1].append(e)

queue = deque()
for i in range(1, N+1):
    if student[i][0] == 0:
        queue.append(i)

route = []
while len(queue) > 0:
    s = queue.popleft()
    for target_s in student[s][1]:
        student[target_s][0] -= 1
        if student[target_s][0] == 0:
            queue.append(target_s)
    route.append(s)

print(' '.join(map(str, route)))

