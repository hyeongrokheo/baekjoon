"""
코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [1차] 캐시
"""


def solution(cacheSize, cities):
    cache = []
    T = 0

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        if city in cache:
            T += 1
            cache.remove(city)
            cache.append(city)
        else:
            T += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache = cache[1:]
                cache.append(city)

    return T

print(solution(1, ["Jeju", 'jeju', 'aa', 'jeju', 'aa', 'jeju']))