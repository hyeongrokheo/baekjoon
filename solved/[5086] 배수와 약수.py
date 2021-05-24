"""
problem tier : Bronze 3 (solved.ac)
"""

while True:
    first, second = map(lambda x: int(x), input().split())

    if first == 0 and second == 0:
        break
    elif first < second and second % first == 0:
        print('factor')
    elif first > second and first % second == 0:
        print('multiple')
    else:
        print('neither')
