"""
problem tier : Gold 4 (solved.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
positive = []
negative = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num > 0:
        positive.append(num)
    else:
        negative.append(num)

positive.sort()
negative.sort()

negative_sum = 0
while len(negative) > 0:
    if len(negative) == 1:
        negative_sum += negative[0]
        negative.pop()
    else:
        if negative[-1] == 0:
            negative = negative[:-2]
        else:
            negative_sum += negative[0] * negative[1]
            negative = negative[2:]

positive_sum = 0
while len(positive) > 0:
    if len(positive) == 1:
        positive_sum += positive[0]
        positive.pop()
    else:
        if positive[-2] == 1:
            positive_sum += positive[-2] + positive[-1]
        else:
            positive_sum += positive[-2] * positive[-1]
        positive = positive[:-2]

print(negative_sum+positive_sum)
