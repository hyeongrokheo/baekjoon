"""
problem tier : Gold 5 (solved.ac)
"""

import sys
input = sys.stdin.readline

def can_move(channel, broken):
    for button in str(channel):
        if int(button) in broken:
            return False
    return True

N = int(input())
M = int(input())
broken_button = []
if M != 0:
    broken_button = list(map(int, input().split()))

static_N = abs(100-N)
move_N = 500000
if can_move(N, broken_button):
    move_N = len(str(N))
else:
    for i in range(1, static_N):
        if N-i >= 0 and can_move(N-i, broken_button):
            move_N = len(str(N-i)) + i
            break
        elif can_move(N+i, broken_button):
            move_N = len(str(N+i)) + i
            break

print(min(static_N, move_N))
