"""
코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS)
"""


def dfs(numbers, i, sum, target):
    if i == len(numbers):
        if sum == target:
            return 1
        else:
            return 0
    else:
        return dfs(numbers, i+1, sum+numbers[i], target) + dfs(numbers, i+1, sum-numbers[i], target)


def solution(numbers, target):
    return dfs(numbers, 0, 0, target)


print(solution([1, 1, 1, 1, 1], 3))  # 5
print(solution([4, 1, 2, 1], 4))  # 2
