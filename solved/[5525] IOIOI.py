"""
problem tier : Silver 2 (solved.ac)
"""

N = int(input())
M = int(input())
S = input()

exp = 'I'
flag = 0
arr = []
for i in range(len(S)):
    s = S[i]
    if s == exp:
        if exp == 'I':
            exp = 'O'
        else:
            exp = 'I'
        flag += 1
        if i == M - 1:
            arr.append(flag)
    else:
        arr.append(flag)
        if s == 'I':
            exp = 'O'
            flag = 1
        else:
            exp = 'I'
            flag = 0



result = 0

for i in arr:
    if i >= 2*N+1:
        result += (i-(2*N+1))//2 + 1
print(result)

