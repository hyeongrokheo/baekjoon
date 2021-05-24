"""
problem tier : Bronze 5 (solved.ac)
"""

H = input()
decimal = 0

num_dict = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

mul = 1
for i in range(len(H)):
    num = H[len(H)-i-1]
    if num in num_dict.keys():
        num = num_dict[num]
    else:
        num = int(num)
    decimal += mul*num
    mul *= 16

print(decimal)
