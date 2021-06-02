"""
problem tier : Gold 4 (solved.ac)
"""

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

prime_list = [True for i in range(10001)]
prime_list[0] = False
prime_list[1] = False

for i in range(2, 102):
    if i:
        mult = 2
        while i*mult <= 10000:
            prime_list[i*mult] = False
            mult += 1

def get_adj_num(num):
    num = list(map(int, str(num)))
    adj_num = []
    for i in range(1, 10):
        if i != num[0]:
            n = i*1000 + num[1]*100 + num[2]*10 + num[3]
            if prime_list[n]:
                adj_num.append(n)
    for i in range(10):
        if i != num[1]:
            n = num[0]*1000 + i*100 + num[2]*10 + num[3]
            if prime_list[n]:
                adj_num.append(n)
    for i in range(10):
        if i != num[2]:
            n = num[0]*1000 + num[1]*100 + i*10 + num[3]
            if prime_list[n]:
                adj_num.append(n)
    for i in range(10):
        if i != num[3]:
            n = num[0]*1000 + num[1]*100 + num[2]*10 + i
            if prime_list[n]:
                adj_num.append(n)

    return adj_num

while T:
    T -= 1
    start, target = map(int, input().split())
    Q = deque()
    Q.append((start, 0))
    visited = [False for i in range(10001)]
    result = 'Impossible'
    while len(Q) > 0:
        num, depth = Q.popleft()
        if visited[num]:
            continue
        visited[num] = True
        if num == target:
            result = depth
            break
        for new_num in get_adj_num(num):
            Q.append((new_num, depth+1))
    print(result)
