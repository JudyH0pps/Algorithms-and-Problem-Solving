import sys

input = lambda: sys.stdin.readline().rstrip()
# f = open('input.txt', 'r')
# input = lambda: f.readline().rstrip()

N = int(input())

if N % 2:
    print(0)
else:
    L = max(2, N)
    dp = [[0] * L for _ in range(2)]
    dp[0][0] = 1
    dp[0][1] = 2
    for i in range(2, N):
        dp[0][i] = dp[0][i - 1] + dp[0][i - 2]
    for i in range(1, N, 2):
        x = 1
        if i - 2 >= 0:
            x = dp[1][i - 2]
        dp[1][i] += x * 3
        for j in range(i - 4, -2, -2):
            y = 1
            if j >= 0:
                y = dp[1][j]
            dp[1][i] += y * 2
        # print(dp)
    print(dp[1][N - 1])
