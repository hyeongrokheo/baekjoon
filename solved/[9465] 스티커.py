"""
problem tier : Silver 2 (solved_old.ac)
"""

T = int(input())

while T:
    T -= 1

    n = int(input())
    sticker = []
    sticker.append(list(map(lambda x: int(x), input().split())))
    sticker.append(list(map(lambda x: int(x), input().split())))

    dp = [[None for i in range(n)] for j in range(3)]
    for i in range(n):
        if i == 0:
            dp[0][0] = sticker[0][0]
            dp[1][0] = sticker[1][0]
            dp[2][0] = 0
        else:
            dp[0][i] = max([dp[1][i-1], dp[2][i-1]]) + sticker[0][i]
            dp[1][i] = max([dp[0][i-1], dp[2][i-1]]) + sticker[1][i]
            dp[2][i] = max([dp[0][i-1], dp[1][i-1], dp[2][i-1]])

    print(max([dp[0][n-1], dp[1][n-1], dp[2][n-1]]))

