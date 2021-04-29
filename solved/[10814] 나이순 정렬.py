"""
problem tier : Silver 5 (solved_old.ac)
"""

N = int(input())

age_arr = [[] for i in range(201)]

for i in range(N):
    inp = input()
    age, name = int(inp.split()[0]), inp.split()[1]

    age_arr[age].append(name)

for i in range(len(age_arr)):
    for name in age_arr[i]:
        print(i, name)
