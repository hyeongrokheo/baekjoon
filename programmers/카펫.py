"""
코딩테스트 연습 > 완전탐색
"""


def solution(brown, yellow):
    A = 3
    while True:
        B = (brown + 4 - 2 * A) // 2

        if A*B - 2*A - 2*B + 4 == yellow:
            return [max(A, B), min(A, B)]

        A += 1
