"""
코딩테스트 연습 > 2018 KAKAO BLIND RECRUITMENT > [1차] 셔틀버스
"""

def solution(n, t, m, timetable):
    timetable = list(map(lambda x: int(x.split(':')[0])*60 + int(x.split(':')[1]), timetable))
    timetable.sort()

    bus_time = 540
    for i in range(n):
        bus = []
        for j in range(m):
            if len(timetable) == 0:
                continue
            if timetable[0] <= bus_time:
                bus.append(timetable[0])
                timetable.pop(0)
            else:
                break

        bus_time += t
    bus_time -= t
    if len(bus) < m:
        result = bus_time
    else:
        result = max(bus)-1
    result = str(result//60).zfill(2) + ':' + str(result%60).zfill(2)
    return result


# print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
# print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
# print(solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
