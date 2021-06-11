"""
problem tier : Gold 5 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')

inp = sys.stdin.readlines()
N = len(inp)

trees = {}
for tree in inp:
    tree = tree.strip()
    if tree in trees.keys():
        trees[tree] += 1
    else:
        trees[tree] = 1

keys = list(trees.keys())
keys.sort()
for t in keys:
    print('{} {:.4f}'.format(t, trees[t] / N * 100))
