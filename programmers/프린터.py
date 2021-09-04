"""
코딩테스트 연습 > 스택/큐 > 프린터
"""

from collections import deque

def solution(priorities, location):
    priorities = list(map(lambda x: (priorities[x], x), range(len(priorities))))
    Q = deque(priorities)

    count = 1
    while True:
        paper, index = Q.popleft()
        print(paper, index)
        if len(Q) != 0 and paper < max(Q, key=lambda x: x[0])[0]:
            Q.append((paper, index))
        else:
            if index == location:
                return count
            else:
                count += 1
