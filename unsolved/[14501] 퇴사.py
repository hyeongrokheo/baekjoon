"""
problem tier : Silver 4 (solved_old.ac)
"""

import sys
# sys.stdin = open('./input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
time = []
benefit = []
for i in range(N):
    t, b = map(lambda x: int(x), sys.stdin.readline().split())
    if i + t > N:
        b = 0
    time.append(t)
    benefit.append(b)
time.reverse()
benefit.reverse()
# print(time)
# print(benefit)
# exit()
# dp = benefit
for i in range(N):
    if i >= time[i]:
        benefit[i] = max(benefit[i-time[i]]+benefit[i], benefit[i-1])
    print(benefit)

print(max(benefit))
