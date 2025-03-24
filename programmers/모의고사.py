"""
코딩테스트 연습 > 완전탐색
"""


def solution(answers):
    num = len(answers)

    ans_1 = [1, 2, 3, 4, 5] * (num // 5 + 1)
    ans_2 = [2, 1, 2, 3, 2, 4, 2, 5] * (num // 8 + 1)
    ans_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (num // 10 + 1)

    scores = [[0, 0], [1, 0], [2, 0]]

    for i in range(num):
        answer = answers[i]
        if answer == ans_1[i]:
            scores[0][1] += 1
        if answer == ans_2[i]:
            scores[1][1] += 1
        if answer == ans_3[i]:
            scores[2][1] += 1

    top_score = max(scores, key = lambda x: x[1])[1]

    result = list(map(lambda x: x[0]+1, filter(lambda x: x[1] == top_score, scores)))

    return result
