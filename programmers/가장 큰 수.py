"""
코딩테스트 연습 > 정렬
"""


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    numbers = list(map(str, map(int, numbers)))
    res = ''.join(numbers)
    res = str(int(res))

    return res
