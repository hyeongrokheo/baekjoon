N = int(input())

if N == 1:
    exit()

def isPrime(X):
    if X == 1:
        return False
    elif X == 2:
        return True
    for i in range(X-2):
        if X % (i+2) == 0:
            return False
    return True


prime = 2
while not isPrime(N):
    if N%prime == 0:
        print(prime)
        N = N//prime
    else:
        prime += 1
        while not isPrime(prime):
            prime += 1
print(N)
