"""
problem tier : Silver 2 (solved_old.ac)
"""

stack = []

def search(d):
    if d == 6:
        print(' '.join(map(lambda x: str(x), stack)))
    else:
        for s in S:
            if d == 0 or stack[-1] < s:
                stack.append(s)
                search(d+1)
                stack.pop()


while True:
    inp = list(map(lambda x: int(x), input().split()))
    if inp[0] == 0:
        break
    else:
        global S
        k = inp[0]
        S = inp[1:]
        search(0)
        print()

