"""
problem tier : Silver 3 (solved.ac)
"""

N, M = map(lambda x: int(x), input().split())

stack = []


def NM():
    if len(stack) == M:
        print(' '.join(map(str, stack)))
    else:
        for i in range(1, N+1):
            if len(stack) == 0 or i >= stack[-1]:
                stack.append(i)
                NM()
                stack.pop()


NM()
