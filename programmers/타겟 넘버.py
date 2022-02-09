"""
코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 타겟 넘버
"""

result = 0
current_num = 0
numbers = []
target = 0


def search(index, num):
    global current_num, result, numbers
    # print(index, num)
    if index == len(numbers):
        if num == target:
            result += 1
        return

    search(index+1, num+numbers[index])
    search(index+1, num-numbers[index])


def solution(_numbers, _target):
    global numbers, target, result
    numbers = _numbers
    target = _target
    search(0, 0)
    return result


print(solution([1, 1, 1, 1, 1], 3))