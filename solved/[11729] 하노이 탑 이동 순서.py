"""
problem tier : Silver 2 (solved.ac)
"""

N = int(input())
paths = []
count = 0

def hanoi(n, src, dst):
    rmn = 6-src-dst
    if n == 1:
        paths.append([src, dst])
        return 1
    else:
        return hanoi(n-1, src, rmn) + hanoi(1, src, dst) + hanoi(n-1, rmn, dst)

print(hanoi(N, 1, 3))
# for path in paths:
#     print(path[0], path[1])