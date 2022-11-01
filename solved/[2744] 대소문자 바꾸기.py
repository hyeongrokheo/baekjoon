"""
problem tier : Bronze 5 (solved.ac)
"""


def solution():
    print(''.join(map(lambda x: x.lower() if x.isupper() else x.upper(), input())))


solution()
