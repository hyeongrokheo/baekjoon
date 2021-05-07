"""
problem tier : Silver 3 (solved_old.ac)
"""

N, M = map(lambda x: int(x), input().split())
num = list(map(lambda x: int(x), input().split()))
num.sort()

stack = []

def NM():
    if len(stack) == M:
        print(' '.join(map(str, stack)))
    else:
        for i in num:
            if len(stack) == 0 or i not in stack:
                stack.append(i)
                NM()
                stack.pop()


NM()
