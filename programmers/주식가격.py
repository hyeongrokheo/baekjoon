"""
코딩테스트 연습 > 스택/큐
"""

def solution(prices):
    stack = []

    result = [None for _ in range(len(prices))]

    for i in range(len(prices)):
        p = prices[i]
        while len(stack) != 0 and stack[-1][1] > p:
            result[stack[-1][0]] = i - stack[-1][0]
            stack.pop()
        stack.append((i, p))

    return [result[i] if result[i] else len(result)-i-1 for i in range(len(result))]
