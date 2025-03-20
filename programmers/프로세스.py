"""
코딩테스트 연습 > 스택/큐
"""


def solution(priorities, location):
    task = []

    for i in range(len(priorities)):
        task.append((i, priorities[i]))
    priorities.sort()

    count = 1
    while len(task) > 0:
        current = task[0]
        if current[1] >= priorities[-1]:
            if current[0] == location:
                return count
            task = task[1:]
            priorities.pop()
            count += 1
        else:
            task = task[1:]
            task.append(current)
