"""
코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > 다트 게임
"""


def solution(dartResult):
    score_list = []
    dartResult = dartResult.replace('10', 'A')
    while len(dartResult) != 0:
        # print(dartResult)
        score = dartResult[0]
        if score == 'A':
            score = '10'
        score = int(score)
        bonus = dartResult[1]
        special = '-'
        if len(dartResult) >= 3 and dartResult[2] in ['*', '#']:
            special = dartResult[2]
        score_list.append([score, bonus, special])

        if special == '-':
            dartResult = dartResult[2:]
        else:
            dartResult = dartResult[3:]

    score_calc = []
    for score in score_list:
        if score[1] == 'S':
            s = score[0]
        elif score[1] == 'D':
            s = score[0] ** 2
        else:
            s = score[0] ** 3

        if score[2] == '#':
            s = -s
        elif score[2] == '*':
            s *= 2
            if len(score_calc) != 0:
                score_calc[-1] *= 2

        score_calc.append(s)

    return sum(score_calc)


print(solution('1S2D*3T'))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))
