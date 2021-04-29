arr = list(map(lambda x: int(x), input().split()))

result = 0
for i in arr:
    result += i**2

print(int(result % 10))
