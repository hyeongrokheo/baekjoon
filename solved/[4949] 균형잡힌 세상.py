"""
problem tier : Silver 4 (solved_old.ac)
"""

while True:
    sentence = input()
    # print(sentence)
    if sentence == '.':
        break

    stack = []
    for token in sentence:
        if token == '[' or token == '(':
            stack.append(token)
        elif token == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                break
        elif token == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                break
        elif token == '.':
            if len(stack) == 0:
                print('yes')
            else:
                print('no')
            continue
