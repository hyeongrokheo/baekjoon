"""
problem tier : Silver 2 (solved.ac)
"""

N, S = map(lambda x: int(x), input().split())
arr = list(map(lambda x: int(x), input().split()))

stack = []
count = 0
def dfs(n, s):
    global count
    if n == N:
        if s == S and len(stack) != 0:
            count += 1
    else:
        stack.append(arr[n])
        dfs(n+1, s+arr[n])
        stack.pop()
        dfs(n+1, s)

dfs(0, 0)
print(count)
