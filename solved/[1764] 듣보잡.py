"""
problem tier : Silver 4 (solved.ac)
"""

N, M = map(lambda x: int(x), input().split())

unheard = []
unseen = []

for i in range(N):
    unheard.append(input())
for i in range(M):
    unseen.append(input())

unheard.sort()
unseen.sort()

count = 0
n, m = 0, 0
dbjs = []
while n < N and m < M:
    if unheard[n] == unseen[m]:
        dbjs.append(unheard[n])
        count += 1
        n += 1
        m += 1
    elif unheard[n] > unseen[m]:
        m += 1
    else:
        n += 1

print(count)
for dbj in dbjs:
    print(dbj)
