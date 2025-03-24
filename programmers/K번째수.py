"""
코딩테스트 연습 > 정렬
"""


def solution(array, commands):
    return [sorted(array[command[0]-1:command[1]])[command[2]-1] for command in commands]
