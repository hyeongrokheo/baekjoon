import itertools

result = list(itertools.product([1, 2, 3], repeat=9))

print(result, len(result))
