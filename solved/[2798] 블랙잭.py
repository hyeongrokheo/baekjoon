"""
problem tier : Bronze 2 (solved.ac)
"""

N, M = map(lambda x: int(x), input().split())

cards = list(map(lambda x: int(x), input().split()))

best = 0

for i in range(N):
    if cards[i] >= M:
        continue
    for j in range(i+1, N):
        if cards[i]+cards[j] >= M:
            continue
        for k in range(j+1, N): # sort 후 binary search로 변경시 시간복잡도 감소.(N^3 -> N^2 * logN)
            # print(cards[i], cards[j], cards[k], ':', cards[i]+cards[j]+cards[k])
            # print(best)
            if cards[i]+cards[j]+cards[k] <= M:
                if best < cards[i]+cards[j]+cards[k]:
                    best = cards[i]+cards[j]+cards[k]

print(best)
