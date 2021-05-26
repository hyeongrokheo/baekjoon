"""
problem tier : Gold 4 (solved.ac)
"""

chars = [0 for i in range(26)]

N = int(input())
for i in range(N):
    word = input().strip()
    for j in range(len(word)):
        chars[ord(word[j]) - ord('A')] += 10**(len(word)-j-1)

chars.sort(reverse=True)
result = 0
for i in range(9):
    result += chars[i] * (9-i)

print(result)
