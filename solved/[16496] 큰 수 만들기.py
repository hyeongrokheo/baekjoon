"""
problem tier : Platinum 5 (solved.ac)
"""

from functools import cmp_to_key
import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = input().split()


def compare(a, b):
    if a+b > b+a:
        return -1
    else:
        return 1


arr.sort(key=cmp_to_key(compare))
result = ''.join(arr)
if result[0] == '0':
    result = '0'
print(result)
