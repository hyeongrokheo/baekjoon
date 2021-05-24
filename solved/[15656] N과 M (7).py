"""
problem tier : Silver 3 (solved.ac)
"""

N, M = map(lambda x: int(x), input().split())
num = list(map(lambda x: int(x), input().split()))
num.sort()

stack = []

def NM():
    if len(stack) == M:
        print(' '.join(map(str, stack)))
    else:
        for n in num:
            stack.append(n)
            NM()
            stack.pop()

NM()
