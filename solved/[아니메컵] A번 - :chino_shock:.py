"""
problem tier : XXX X (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')


def solution():
    emoji = input()
    print(len(emoji) + emoji.count(':') + emoji.count('_') * 5)


solution()
