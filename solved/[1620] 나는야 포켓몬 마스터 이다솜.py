"""
problem tier : Silver 4 (solved.ac)
"""

import sys

N, M = map(lambda x: int(x), input().split())

pok_to_num = {}
num_to_pok = {}

for i in range(N):
    pok = sys.stdin.readline().strip()
    pok_to_num[pok] = i+1
    num_to_pok[i+1] = pok

for i in range(M):
    inf = sys.stdin.readline().strip()
    if inf.isdigit():
        print(num_to_pok[int(inf)])
    else:
        print(pok_to_num[inf])
