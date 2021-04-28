T = int(input())
while T:
    inp = list(map(int, input().split(' ')))
    H = inp[0]
    W = inp[1]
    N = inp[2]

    print(str(H if N%H == 0 else N%H) + str(N//H if N%H == 0 else N//H + 1).zfill(2))
    T -= 1