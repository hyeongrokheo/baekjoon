"""
코딩테스트 연습 > 탐욕법(Greedy)
"""


def solution(people, limit):
    people.sort(reverse=True)

    seat = []
    two_people_boats = 0

    for p in people:
        if len(seat) > 0 and seat[-1] >= p:
            seat.pop()
            two_people_boats +=1
        else:
            seat.append(limit - p)

    return len(people) - two_people_boats


print(solution([70, 50, 80, 50], 100))  # 3
print(solution([70, 80, 50], 100))  # 3
