"""
problem tier : Platinum 3 (solved.ac)
"""

import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.readline

def update(s, e, n, l, r):
    if s <= l and r <= e:
        None
    elif r < s and e < l:
        None
    else:
        mid = (l+r)//2
        update(s, e, n*2, l, mid)
        update(s, e, n*2+1, mid+1, r)


N, M = map(int, input().split())

seg_tree = [0 for i in range(N * 4)]
lazy_tree = [0 for i in range(N * 4)]
