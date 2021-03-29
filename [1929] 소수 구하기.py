inp = input().split()
M = int(inp[0])
N = int(inp[1])


primeList = []

for i in range(N):
    if i == 0 or i == 1:
        continue
    elif i == 2:
        primeList.append(i)
    else:
        isPrime = True
        for prime in primeList:
            if i % prime == 0:
                isPrime = False
                break
        if isPrime:
            primeList.append(i)


print(primeList)

#
# targetNum = M
#
# while targetNum <= N:
#     if isPrime(targetNum):
#         print(targetNum)
#     targetNum += 1