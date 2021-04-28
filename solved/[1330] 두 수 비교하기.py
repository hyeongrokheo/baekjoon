inp = input().split(' ')
A = int(inp[0])
B = int(inp[1])
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')