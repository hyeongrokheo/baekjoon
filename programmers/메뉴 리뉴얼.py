"""
코딩테스트 연습 > 2021 KAKAO BLIND RECRUITMENT > 메뉴 리뉴얼
"""

from itertools import combinations

def make_comb(order, size):
    order_list = list(order)
    result = list(map(list, (combinations(order_list, size))))
    for i in range(len(result)):
        result[i].sort()
        result[i] = ''.join(result[i])
    result = list(set(result))
    return result


def solution(orders, course):
    menu = [{} for i in range(len(course))]
    for order in orders:
        for size in course:
            comb = make_comb(order, size)
            for c in comb:
                ind = course.index(size)
                if c in menu[ind].keys():
                    menu[ind][c] += 1
                else:
                    menu[ind][c] = 1
    answer = []
    for i in range(len(menu)):
        if len(menu[i]) == 0:
            continue
        target_ref = max(menu[i].values())
        if target_ref < 2:
            continue
        for m in menu[i].keys():
            if menu[i][m] == target_ref:
                answer.append(m)
    answer.sort()

    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))