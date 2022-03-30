"""
problem tier : Gold 4 (solved.ac)
"""

import sys
sys.stdin = open('../input.txt', 'r')


def sort_line(original):
    sorted = []
    count_map = {}
    for e in original:
        if e == 0:
            continue
        if e in count_map.keys():
            count_map[e] += 1
        else:
            count_map[e] = 1
    temp_arr = []
    for key in count_map.keys():
        temp_arr.append((key, count_map[key]))
    temp_arr.sort(key=lambda x: (x[1], x[0]))
    for n, c in temp_arr:
        sorted.append(n)
        if len(sorted) == 100:
            break
        sorted.append(c)
        if len(sorted) == 100:
            break
    return sorted, len(sorted)


def rotate(original):
    rotated = [[] for _ in range(len(original[0]))]

    for i in range(len(original)):
        for j in range(len(original[0])):
            rotated[j].append(original[i][j])

    return rotated


def calc(A):
    max_size = 0
    for i in range(len(A)):
        A[i], size = sort_line(A[i])
        if max_size < size:
            max_size = size
    for i in range(len(A)):
        if len(A[i]) < max_size:
            A[i].extend([0 for _ in range(max_size - len(A[i]))])


def solution():
    r, c, K = map(int, input().split())
    r, c = r-1, c-1
    A = []
    for _ in range(3):
        A.append(list(map(int, input().split())))
    count = 0
    while True:
        if count == 101:
            count = -1
            break

        R = len(A)
        C = len(A[0])
        if r < R and c < C and A[r][c] == K:
            break

        if R >= C:
            calc(A)
        else:
            A = rotate(A)
            calc(A)
            A = rotate(A)

        count += 1

    print(count)


solution()
