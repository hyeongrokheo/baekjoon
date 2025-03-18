"""
코딩테스트 연습 > 해시
"""


def solution(participant, completion):
    d = {}

    for p in participant:
        if p in d.keys():
            d[p] += 1
        else:
            d[p] = 1

    for c in completion:
        d[c] -= 1

    for k, v in d.items():
        if v == 1:
            return k


print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
