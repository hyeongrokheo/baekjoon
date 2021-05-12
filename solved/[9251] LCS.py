"""
problem tier : Gold 5 (solved_old.ac)
"""

str1 = input()
str2 = input()
arr = [[None for i in range(len(str1))] for j in range(len(str2))]

for i in range(len(str2)):
    for j in range(len(str1)):
        # print(str2[i], str1[j])
        if str1[j] == str2[i]:
            if j-1>=0 and i-1>=0:
                arr[i][j] = arr[i-1][j-1]+1
            else:
                arr[i][j] = 1
        else:
            if j-1>=0:
                left = arr[i][j-1]
            else:
                left = 0
            if i-1>=0:
                up = arr[i-1][j]
            else:
                up = 0
            arr[i][j] = max([left, up])

print(arr[len(str2)-1][len(str1)-1])
