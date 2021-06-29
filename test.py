N, P = map(int, input().split())

untrends = []
for i in range(N):
    untrends.append(list(map(int, input().split())))
untrend_P = 0

while len(untrends):
    next_P = list(map(lambda x: [x[0], P*((100-x[1])/100), x[0]+P*((100-x[1])/100)], untrends))
    min_P = min(next_P, key=lambda x: (x[2], -x[1]))
    if P < min_P[2]:
        break

    untrend_P += min_P[0]
    P = min_P[1]
    untrends.remove(untrends[next_P.index(min_P)])

print(untrend_P + P)

###
# 25%
###