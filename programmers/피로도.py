"""
코딩테스트 연습 > 완전탐색
"""

from itertools import permutations


def solution(k, dungeons):
    return max(map(lambda x: calc(k, x), list(permutations(dungeons, len(dungeons)))))


def calc(k, dungeons):
    count = 0
    for dungeon in dungeons:
        if k >= dungeon[0]:
            k -= dungeon[1]
            count += 1
        else:
            return count
    return count
