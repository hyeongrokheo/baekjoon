"""
problem tier : Silver 3 (solved.ac)
"""

N = int(input())
S = []

for i in range(N):
    S.append(list(map(lambda x: int(x), input().split())))

best_dif = 40000
S_team = []

def get_score(team):
    score = 0
    for i in team:
        for j in team:
            if i != j:
                score += S[i][j]
    return score

def team(min_i):
    global best_dif
    if len(S_team) == N//2:
        L_team = []
        for i in range(N):
            if i not in S_team:
                L_team.append(i)
        S_score = get_score(S_team)
        L_score = get_score(L_team)
        dif_score = abs(S_score - L_score)
        if best_dif > dif_score:
            best_dif = dif_score
    else:
        for i in range(min_i, N):
            S_team.append(i)
            team(i+1)
            S_team.remove(i)

team(0)

print(best_dif)
