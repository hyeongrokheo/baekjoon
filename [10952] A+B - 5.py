while True:
    inp = list(map(int, input().split(' ')))
    A = inp[0]
    B = inp[1]
    if A == 0 and B == 0:
        exit()
    print(A + B)