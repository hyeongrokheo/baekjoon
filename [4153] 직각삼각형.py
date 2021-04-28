"""
problem tier : Bronze 3 (solved.ac)
"""

while True:
    inp = input()
    if inp == '0 0 0':
        break
    # inp.
    arr = list(map(lambda x: int(x), inp.split()))
    arr.sort()
    if arr[0] ** 2 + arr[1] ** 2 == arr[2] ** 2:
        print('right')
    else:
        print('wrong')
