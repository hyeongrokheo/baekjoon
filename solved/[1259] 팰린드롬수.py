"""
problem tier : Bronze 1 (solved.ac)
"""

while True:
    num = input()
    if num == '0':
        break

    palin = True
    for i in range(len(num)):
        if num[i] != num[len(num)-1-i]:
            palin = False
            break
    if palin:
        print('yes')
    else:
        print('no')
