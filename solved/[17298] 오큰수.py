"""
problem tier : Gold 4 (solved_old.ac)
"""

N = int(input())

arr = list(map(lambda x: int(x), input().split()))
arr2 = []
for i in range(len(arr)):
    arr2.append([i, arr[i], -1])

stack = []
stock = []
for e in arr2:
    while len(stack) > 0 and e[1] > stack[-1][1]:
        target = stack.pop()
        target[2] = e[1]
        stock.append(target)

    stack.append(e)

stack.extend(stock)
stack.sort(key=lambda x: x[0])
for e in stack:
    print(e[2], end=' ')