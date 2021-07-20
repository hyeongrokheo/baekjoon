"""
problem tier : Bronze 2 (solved.ac)
"""

import sys, math
#sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

N = int(input())
Candidate = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0
for c in Candidate:
    if c <= B:
        result += 1
    else:
        result += 1 + math.ceil((c-B) / C)

print(result)

