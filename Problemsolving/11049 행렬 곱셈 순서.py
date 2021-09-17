import sys
input = sys.stdin.readline

INF = 2 ** 31 - 1
N = int(input())
dp = [[INF] * N for _ in range(N)]
matrix = []
for _ in range(N):
    dp[_][_] = 0
    r, c = map(int, input().split())
    matrix.append([r, c])

for i in range(1, N):
    for j in range(N - i):
        for k in range(j, j + i):
            dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k + 1][j + i] +
                               matrix[j][0] * matrix[k][1] * matrix[j + i][1])

print(dp[0][N - 1])
