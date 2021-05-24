"""
problem tier : Silver 1 (solved.ac)
"""

import sys
sys.setrecursionlimit(10**9)

def bt(left, right):
    if left == right:
        print(data[left])
        return
    elif left > right:
        return
    root = data[left]
    mid = right+1
    for i in range(left+1, right+1):
        if data[i] > root:
            mid = i
            break
    bt(left+1, mid-1)
    bt(mid, right)
    print(root)


data = []
while True:
    try:
        data.append(int(sys.stdin.readline()))
    except:
        break

bt(0, len(data)-1)

