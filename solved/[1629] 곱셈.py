"""
problem tier : Silver 1 (solved_old.ac)
"""

A, B, C = map(lambda x: int(x), input().split())

B = list(map(lambda x: int(x), bin(B)[2:]))
B.reverse()

multiplier = A
result = 1
for i in B:
    # print('mult :', multiplier)
    # result *= multiplier * i % C
    if i == 1:
        result *= multiplier
        result %= C
    multiplier = (multiplier ** 2) % C
    # print('result :', result)

print(result)
