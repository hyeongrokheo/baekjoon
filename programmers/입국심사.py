"""
코딩테스트 연습 > 이분탐색 > 입국심사
"""


times = None


def get_count(time):
    result = 0
    for t in times:
        result += time // t
    return result


def solution(n, _times):
    global times
    times = _times

    left = 0
    right = max(times) * n
    while left <= right:
        mid = (left + right) // 2
        count = get_count(mid)
        if count < n:
            left = mid+1
        elif count > n:
            right = mid-1
        else:
            right = mid-1

    return left


print(solution(11, [4, 5]))
