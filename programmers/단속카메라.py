"""
코딩테스트 연습 > 탐욕법(Greedy)
"""

def solution(routes):
    routes.sort(key=lambda x: (x[1], x[0]))

    camera_num = 0

    while len(routes) > 0:
        camera_spot = routes[0][1]

        routes = list(filter(lambda x: x[0] > camera_spot, routes))
        camera_num += 1

    return camera_num

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))
