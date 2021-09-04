"""
코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [3차] 비밀지도
"""


def solution(n, arr1, arr2):
    result = []
    for i in range(n):
        # for j in range(n):
        # print(arr1[i], arr2[i])
        walls = arr1[i] | arr2[i]
        walls = str(bin(walls))[2:]
        while len(walls) != n:
            walls = '0' + walls
        # print(walls)
        walls = walls.replace('1', '#')
        walls = walls.replace('0', ' ')


        result.append(walls)


    return result


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
# print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
