"""
problem tier : Gold 5 (solved_old.ac)
pypy3
"""

N = int(input())

result = 0


def queen_isable(queen_list):
    if len(queen_list) <= 1:
        return True

    upper_queen = queen_list[:-1]
    bottom_queen = queen_list[-1]

    for i in range(len(upper_queen)):
        # if upper_queen[i] == bottom_queen:
        #     return False
        if abs(len(upper_queen) - i) == abs(bottom_queen - upper_queen[i]):
            return False
    return True

# print(queen_isable([1, 3, 5, 6]))


def queen(queen_list, n):
    # print('queen list :', queen_list)
    if n == N:
        # print(print('queen', queen_list))
        global result
        result += 1
        # None
    else:
        for i in range(N):
            if i in queen_list:
                continue
            queen_list.append(i)
            if queen_isable(queen_list):
                queen(queen_list, n+1)
            queen_list.pop()



queen([], 0)
print(result)
