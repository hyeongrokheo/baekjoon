"""
코딩테스트 연습 > 해시
"""


def solution(nums):
    return min(len(set(nums)), len(nums)//2)


print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))
