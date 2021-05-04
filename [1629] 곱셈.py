"""
problem tier : Silver 1 (solved_old.ac)
"""

A, B, C = map(lambda x: int(x), input().split())
memo = [None] * 32

def get_multiplier(X):
    result = 1
    while 2 ** result <= X:
        result += 1
    result -= 1
    return result

def mul(A, B):
    multiplier = get_multiplier(A)
    if B == 1:
        return A
    elif B == 2:
        return A ** 2 % C
    else:
        return (mul(A, multiplier) * mul(A, B-B//2)) % C

print(mul(A, B))