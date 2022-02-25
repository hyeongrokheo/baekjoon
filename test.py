

N = int(input())
A = list(map(int, input().split()))

# print(N, A)


permutation = []
ancient = [False for i in range(len(A))]
max_permutation = 0
def BT():
    # print(permutation, ancient)
    global max_permutation
    if len(permutation) == N:
        result_permutation = 0
        for i in range(N-1):
            result_permutation += abs(permutation[i] - permutation[i+1])
        if max_permutation < result_permutation:
            max_permutation = result_permutation
        return
    for i in range(len(A)):
        if not ancient[i]:
            ancient[i] = True
            permutation.append(A[i])
            BT()
            permutation.pop()
            ancient[i] = False
BT()
print(max_permutation)






