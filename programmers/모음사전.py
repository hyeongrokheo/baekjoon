"""
코딩테스트 연습 > 완전탐색
"""

from itertools import product


def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    arr = []
    for i in range(1, 6):
        arr.extend(product(vowels, repeat=i))

    arr = list(map(lambda x: ''.join(x), arr))
    arr.sort()

    return arr.index(word) + 1


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))
