"""
problem tier : Silver 1 (solved.ac)
"""

A, B = map(lambda x: int(x), input().split())

count = 1
while True:
    if A == B:
        print(count)
        break
    count += 1
    if B != 1 and B % 10 == 1:
        B = B//10
    elif B % 2 == 0:
        B = B//2
    else:
        if A == B:
            continue
        else:
            print(-1)
            break
