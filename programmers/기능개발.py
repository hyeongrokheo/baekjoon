"""
코딩테스트 연습 > 스택/큐
"""


def solution(progresses, speeds):
    stack = []
    res = []

    for i in range(len(progresses)):
        p = progresses[i]
        s = speeds[i]

        remain = (100-p)//s
        if (100-p)%s != 0:
            remain += 1

        if len(stack) == 0 or remain <= stack[0]:
            stack.append(remain)
        else:
            res.append(len(stack))
            stack = [remain]

    if len(stack) != 0:
        res.append(len(stack))

    return res
