"""
problem tier : Bronze 1 (solved.ac)
"""


def solution():
    input()
    logics = list(map(int, input().split()))

    true_count = 0
    for logic in logics:
        if logics.count(logic) == logic:
            true_count = max(true_count, logic)

    print(-1) if true_count == 0 and 0 in logics else print(true_count)


solution()
