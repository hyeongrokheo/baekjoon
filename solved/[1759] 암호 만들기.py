"""
problem tier : Gold 5 (solved.ac)
"""

L, C = map(lambda x: int(x), input().split())
arr = input().split()
arr.sort()

vowels = ['a', 'e', 'i', 'o', 'u']
stack = []


def bt(index, v, c):
    if v+c == L:
        if v >= 1 and c >= 2:
            print(''.join(map(lambda x: str(x), stack)))
    else:
        for i in range(index+1, len(arr)):
            target_char = arr[i]
            stack.append(target_char)
            if target_char in vowels:
                bt(i, v+1, c)
            else:
                bt(i, v, c+1)
            stack.pop()

bt(-1, 0, 0)
