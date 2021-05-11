import sys
sys.stdin = open('input.txt')


notes = list(map(int, input().split()))

N = len(notes)
INF = 5000000
graph = [
    [INF, 2, 2, 2, 2],
    [INF, 1, 3, 4, 3],
    [INF, 3, 1, 3, 4],
    [INF, 4, 3, 1, 3],
    [INF, 3, 4, 3, 1]
]

dp = [[[0] * 5 for _ in range(5)] for _ in range(N)]

for level in range(N - 2, -1, -1):
    nextNote = notes[level]
    for l in range(5):
        for r in range(5):
            lcost = graph[l][nextNote]
            rcost = graph[r][nextNote]
            dp[level][l][r] = min(
                lcost + dp[level + 1][nextNote][r],
                rcost + dp[level + 1][l][nextNote]
            )

print(dp[0][0][0])
