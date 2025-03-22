"""
코딩테스트 연습 > 스택/큐
"""

def solution(bridge_length, weight, truck_weights):
    bridge = [None for _ in range(bridge_length)]

    bridge_weight_sum = 0
    count = 0
    while True:
        count += 1
        last = bridge.pop()
        if last:
            bridge_weight_sum -= last

        if len(truck_weights) != 0:
            target_truck = truck_weights[0]

            if target_truck <= weight - bridge_weight_sum:
                truck_weights = truck_weights[1:]
                bridge_weight_sum += target_truck
                bridge = [target_truck] + bridge
            else:
                bridge = [None] + bridge

        if bridge_weight_sum == 0:
            return count
