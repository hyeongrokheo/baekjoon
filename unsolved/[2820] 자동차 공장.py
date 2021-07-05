"""
problem tier : Platinum 3 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

def update():

def query():


N, M = map(int, input().split())
salary = [None for i in range(N+1)]
subord = [[] for i in range(N+1)]
seg_tree = [0 for i in range(N*4)]
lazy_tree = [0 for i in range(N*4)]

for i in range(N):
    if i == 0:
        salary[i+1] = int(input())
    else:
         s, u = map(int, input().split())
         salary[i+1] = s
         subord[u].append(i+1)
