"""
problem tier : Silver 3 (solved.ac)
"""

N, M = map(lambda x: int(x), input().split())

# arr = [False] * N

stack = []


def NM():
    if len(stack) == M:
        print(' '.join(map(str, stack)))
    else:
        for i in range(1, N+1):
            if i not in stack:
                stack.append(i)
                NM()
                stack.pop()

NM()
