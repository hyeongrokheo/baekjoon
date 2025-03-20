"""
코딩테스트 연습 > 스택/큐
"""


def solution(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0 or stack[-1] == ')':
                return False
            else:
                stack.pop()
    return len(stack) == 0
