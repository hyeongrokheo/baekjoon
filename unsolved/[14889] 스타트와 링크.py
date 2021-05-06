"""
problem tier : Silver 3 (solved_old.ac)
"""

N = int(input())
S = []
S_sum = 0
for i in range(N):
    L = list(map(lambda x: int(x), input().split()))
    S.append(L)
    S_sum += sum(L)
# print(S_sum)
# exit()
# print(S)

best_dif = 40000
members = []

score = 0
def team(min_i):
    # print(members)
    global best_dif
    global score
    if len(members) == N//2:
        dif_score = abs(S_sum-score*2)
        if best_dif > dif_score:
            best_dif = dif_score
        print(members)
        print(best_dif)
        return

    for i in range(min_i, N):
        if i not in members:
            plus_score = 0
            for j in members:
                plus_score += S[i][j] + S[j][i]
            score += plus_score
            members.append(i)
            team(i+1)
            score -= plus_score
            members.pop()

team(0)

print(best_dif)