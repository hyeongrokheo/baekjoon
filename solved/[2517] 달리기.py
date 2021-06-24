"""
problem tier : Platinum 4 (solved.ac)
"""

from copy import deepcopy
import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


def update(x, y, n, l, r):
    # print(x, y, n, l, r)
    if l == r:
        seg_tree[n] = y
        return 1
    else:
        seg_tree[n] += 1
        mid = (l+r) // 2
        if x <= mid:
            return seg_tree[n*2+1] + update(x, y, n*2, l, mid)
        else:
            return update(x, y, n*2+1, mid+1, r)


N = int(input())
players = []
for i in range(N):
    players.append(int(input()))

temp_players = deepcopy(players)
temp_players.sort()
compr = {}
for i in range(N):
    compr[temp_players[i]] = i+1
for i in range(N):
    players[i] = compr[players[i]]

seg_tree = [0 for i in range(N*4)]
for p in players:
    print(update(p, 1, 1, 1, N))
