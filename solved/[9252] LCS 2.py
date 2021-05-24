"""
problem tier : Gold 5 (solved.ac)
"""

S1 = input()
S2 = input()

dp = [['' for j in range(len(S2))] for i in range(len(S1))]

for i in range(len(S1)):
    for j in range(len(S2)):
        if S1[i] == S2[j]:
            if i > 0 and j > 0:
                dp[i][j] = dp[i-1][j-1] + S1[i]
            else:
                dp[i][j] = S1[i]
        else:
            left = ''
            if j >= 1:
                left = dp[i][j-1]
            up = ''
            if i >= 1:
                up = dp[i-1][j]
            if len(left) > len(up):
                dp[i][j] = left
            else:
                dp[i][j] = up

print(len(dp[len(S1)-1][len(S2)-1]))
print(dp[len(S1)-1][len(S2)-1])
