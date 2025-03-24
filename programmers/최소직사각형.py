"""
코딩테스트 연습 > 완전탐색
"""


def solution(sizes):
    sizeA = 0
    sizeB = 0

    for size in sizes:
        sizeA = max(sizeA, max(size[0], size[1]))
        sizeB = max(sizeB, min(size[0], size[1]))

    return sizeA * sizeB

