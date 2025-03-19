"""
코딩테스트 연습 > 해시
"""


def solution(clothes):
    hash_map = {}

    for c in clothes:
        if c[1] in hash_map.keys():
            hash_map[c[1]].append(c[0])
        else:
            hash_map[c[1]] = [c[0]]

    res = 1
    for v in hash_map.values():
        res = res * (len(v) + 1)

    return res - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
