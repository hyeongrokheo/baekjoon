def print_star(length, star):
    empty_length = int((length - star) / 2)
    for _ in range(empty_length):
        print(' ', end='')
    for _ in range(star):
        print('*', end='')
    print()

N = int(input())

for i in range(N):
    print_star(N * 2 - 1, (N-i) * 2 - 1)

for i in range(N-1):
    print_star(N * 2 - 1, i * 2 + 3)