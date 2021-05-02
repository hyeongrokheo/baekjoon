"""
problem tier : Silver 1 (solved_old.ac)
"""

N = int(input())
num_arr = list(map(lambda x: int(x), input().split()))
oper_arr = list(map(lambda x: int(x), input().split()))
max_num = -1000000000
min_num = 1000000000

def calc(result) :
    global num_arr
    if len(num_arr) == 0:
        global max_num, min_num
        if max_num < result:
            max_num = result
        if min_num > result:
            min_num = result
        return
    if oper_arr[0] > 0:
        num = num_arr[0]
        num_arr = num_arr[1:]
        oper_arr[0] -= 1
        calc(result + num)
        num_arr.insert(0, num)
        oper_arr[0] += 1
    if oper_arr[1] > 0:
        num = num_arr[0]
        num_arr = num_arr[1:]
        oper_arr[1] -= 1
        calc(result - num)
        num_arr.insert(0, num)
        oper_arr[1] += 1
    if oper_arr[2] > 0:
        num = num_arr[0]
        num_arr = num_arr[1:]
        oper_arr[2] -= 1
        calc(result * num)
        num_arr.insert(0, num)
        oper_arr[2] += 1
    if oper_arr[3] > 0:
        num = num_arr[0]
        num_arr = num_arr[1:]
        oper_arr[3] -= 1
        if result < 0:
            result *= -1
            calc(-1 * (result // num))
        else:
            calc(result // num)
        num_arr.insert(0, num)
        oper_arr[3] += 1

start = num_arr[0]
num_arr = num_arr[1:]
calc(start)
print(max_num)
print(min_num)