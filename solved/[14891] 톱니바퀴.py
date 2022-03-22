"""
problem tier : Gold 5 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')
input = sys.stdin.readline


chain = []


def shift_chain(original, direction):
    if direction == -1:
        shifted = original[1:]
        shifted.append(original[0])
    else:
        shifted = [original[-1]]
        shifted.extend(original[:-1])
    # print(shifted)
    return shifted

# shift_chain([1,2,3,4], 1)
# shift_chain([1,2,3,4], -1)


def move_chain(chain_num, direction, chain_from):
    target_point_right = chain[chain_num][2]
    target_point_left = chain[chain_num][6]
    chain[chain_num] = shift_chain(chain[chain_num], direction)
    if chain_num == chain_from:
        if chain_num != 0 and chain[chain_num-1][2] != target_point_left:
            move_chain(chain_num-1, -direction, chain_num)
        if chain_num != 3 and chain[chain_num+1][6] != target_point_right:
            move_chain(chain_num+1, -direction, chain_num)
    elif chain_num == chain_from + 1:  # 오른쪽 방향으로 톱니 진행
        if chain_num != 3 and chain[chain_num+1][6] != target_point_right:
            move_chain(chain_num+1, -direction, chain_num)
    else:
        if chain_num != 0 and chain[chain_num - 1][2] != target_point_left:
            move_chain(chain_num-1, -direction, chain_num)



def solution():
    global chain

    for i in range(4):
        chain.append(list(map(int, input().strip())))

    K = int(input())
    for i in range(K):

        a, b = map(int, input().split())
        move_chain(a-1, b, a-1)

    score = chain[0][0] * 1 + chain[1][0] * 2 + chain[2][0] * 4 + chain[3][0] * 8
    # print(chain)
    print(score)


solution()
