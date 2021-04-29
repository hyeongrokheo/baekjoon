def is_prime(num):
    if num == 1:
        return False
    for i in range(num):
        if i <= 1:
            continue
        if num % i == 0:
            return False
    return True


N = int(input())
M = int(input())

min_prime_num = 10000
sum_prime_num = 0

for i in range(M-N+1):
    target_num = N + i
    if is_prime(target_num):
        if min_prime_num > target_num:
            min_prime_num = target_num
        sum_prime_num += target_num

if sum_prime_num == 0:
    print(-1)
else:
    print(sum_prime_num)
    print(min_prime_num)