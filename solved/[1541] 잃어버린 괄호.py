"""
problem tier : Silver 2 (solved_old.ac)
"""

sen = input()
split = sen.find('-')
if split == -1:
    print(sum(list(map(lambda x: int(x), sen.replace('-', '+').split('+')))))
else:
    positive = sum(list(map(lambda x: int(x), sen[:split].replace('-', '+').split('+'))))
    negative = sum(list(map(lambda x: int(x), sen[split + 1:].replace('-', '+').split('+'))))
    print(positive - negative)