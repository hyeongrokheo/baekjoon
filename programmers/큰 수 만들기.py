"""
코딩테스트 연습 > 탐욕법(Greedy)
"""


def solution(number, k):
    stack = []
    for n in number:
        if k == 0 or len(stack) == 0:
            stack.append(n)
        elif k > 0:
            while len(stack) > 0 and stack[-1] < n and k > 0:
                stack.pop()
                k -= 1
            stack.append(n)

    if k > 0:
        stack = stack[:-k]
    return ''.join(stack)


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("11", 1))
