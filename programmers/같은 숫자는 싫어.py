"""
코딩테스트 연습 > 스택/큐
"""


def solution(arr):
    new_arr = []
    for a in arr:
        if len(new_arr) == 0:
            new_arr.append(a)
        elif new_arr[-1] != a:
            new_arr.append(a)

    return new_arr

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))
