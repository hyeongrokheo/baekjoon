
result = [[], []]
for i in range(3):
    inp = list(map(lambda x:int(x), input().split()))
    x = inp[0]
    y = inp[1]

    if x in result[0]:
        result[0].remove(x)
    else:
        result[0].append(x)

    if y in result[1]:
        result[1].remove(y)
    else:
        result[1].append(y)

print(result[0][0], result[1][0])


