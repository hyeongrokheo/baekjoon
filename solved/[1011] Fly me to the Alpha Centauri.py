"""
problem tier : Silver 1 (solved_old.ac)
"""

T = int(input())
# T = 10
while T:
    inp = list(map(int, input().split(' ')))
    start_point = inp[0]
    end_point = inp[1]

    current_state = 0
    current_speed = 0
    target_state = end_point - start_point
    step_count = 0
    while target_state >= current_state * 2 + current_speed + 1:
        step_count += 1
        current_speed += 1
        current_state += current_speed
        # print('step count =', step_count)
        # print('speed =', current_speed)
        # print('current state =', current_state)
    step_count = step_count * 2 - 1
    current_state = 2 * current_state - current_speed
    rest_distance = target_state - current_state
    # print('rest distance =', rest_distance)
    # print(step_count)
    if rest_distance == 0:
        print(step_count)
    elif rest_distance > 0:
        if rest_distance > current_speed:
            print(step_count + 2)
        else:
            print(step_count + 1)
    # else:
    #     print(step_count + 1)
    # print(step_count if rest_distance == 0 else step_count+1)
    T -= 1