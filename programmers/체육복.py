"""
코딩테스트 연습 > 탐욕법(Greedy)
"""

from copy import deepcopy


def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    r_lost = deepcopy(lost)
    lost = list(filter(lambda x: x not in reserve, lost))
    reserve = list(filter(lambda x: x not in r_lost, reserve))

    real_lost = 0
    for l in lost:
        if l-1 in reserve:
            reserve.remove(l-1)
        elif l+1 in reserve:
            reserve.remove(l+1)
        else:
            real_lost += 1
    return n - real_lost


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
print(solution(5, [4, 2], [3, 5]))
