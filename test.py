"""
arr[레인 번호-1]=[장애물 위치들...]
형식으로 변경시 간단한 시뮬레이션 구현으로 해결 가능
"""

from collections import deque


# def cookie_run(lane, start_lane, )

def run_next(lane, position):
    for i in range(len(lane)):
        if position < lane[i]:
            return True, i
    return False, 0


def solution(K, A):
    print(K, A)
    lane = [[] for i in range(K)]
    position = 1
    for i in A:
        lane[i - 1].append(position)
        position += 1

    count = 0
    while len(lane) > 0:
        if len(lane[0]) == 0:  # 장애물 없는 레인 지워나가기
            lane = lane[1:]
            continue

        i = 0
        crash, crash_index = run_next(lane[0], 0)
        # position = lane[i][0]  # 첫 레인의 첫 번째 장애물
        # crash = True
        while crash:
            i += 1
            if len(lane) == i:
                break
            crash, crash_index = run_next(lane[i], position)  # 달리고, 장애물 충돌 여부와 위치 반환
            if crash:
                lane[i].pop(crash_index)  # 충돌한 장애물 지우기

        count += 1

    return count

print(solution(5, [1,3,4,2,5]))