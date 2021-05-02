"""
problem tier : Silver 3 (solved_old.ac)
"""

K, N = map(lambda x: int(x), input().split())

lan = []
for i in range(K):
    lan.append(int(input()))

def get_lan(length):
    result = 0
    for l in lan:
        result += l // length
    return result

left = 1
right = 10000000000
while left != right:
    standard = (right + left + 1) // 2
    newlan = get_lan(standard)
    if N <= newlan:
        left = standard
    else:
        right = standard - 1

print(right)
