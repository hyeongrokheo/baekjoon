"""
problem tier : Bronze 1 (solved.ac)
"""

# import sys
# sys.stdin = open('./input.txt', 'r')


def count_0(num):
    return str(num).count('0')


def solution():
    T = int(input())
    while T:
        T -= 1
        N, M = map(int, input().split())
        sum_count_0 = 0
        for num in range(N, M+1):
            sum_count_0 += count_0(num)
        print(sum_count_0)


solution()
