"""
코딩테스트 연습 > 2019 KAKAO BLIND RECRUITMENT > 오픈채팅방
"""


def solution(record):
    id_to_name = {}
    operation = []
    for r in record:
        r = r.split(' ')
        state = r[0]
        id = r[1]
        if state == 'Leave':
            name = '-'
        else:
            name = r[2]

        if state == 'Enter':
            operation.append([state, id])
            id_to_name[id] = name
        elif state == 'Leave':
            operation.append([state, id])
        else:
            id_to_name[id] = name
    result = []
    for op in operation:
        if op[0] == 'Enter':
            result.append('{}님이 들어왔습니다.'.format(id_to_name[op[1]]))
        else:
            result.append('{}님이 나갔습니다.'.format(id_to_name[op[1]]))

    return result

print(solution(["Enter uid1234 Muzi",
                "Enter uid4567 Prodo",
                "Leave uid1234",
                "Enter uid1234 Prodo",
                "Change uid4567 Ryan"]))
