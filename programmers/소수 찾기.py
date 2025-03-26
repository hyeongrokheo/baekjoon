"""
코딩테스트 연습 > 완전탐색
"""

from itertools import permutations
from math import sqrt


def solution(numbers):
    cases = []

    for i in range(len(numbers)):
        cases += list(permutations(numbers, i+1))

    for c in cases:
        num = ''.join(c)

    nums = list(set(map(lambda x: int(''.join(x)), cases)))
    nums = list(filter(is_prime, nums))

    return len(nums)

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
