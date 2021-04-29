"""
problem tier : Silver 5 (solved_old.ac)
"""

N = int(input())

arr = []
for i in range(N):
    arr.append(input())

arr = list(set(arr))
arr.sort(key=lambda x: (len(x), x))

for word in arr:
    print(word)
