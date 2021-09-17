import sys
sys.stdin = open('input.txt')

INF = (1 << 31) - 1
T = int(input())

for _ in range(T):
    K = int(input())
    arr = list(map(int, input().split()))
    dp = [[INF] * len(arr) for _ in range(len(arr))]
    cumulsum = [[0] * len(arr) for _ in range(len(arr))]

    for i in range(len(arr)):
        dp[i][i] = 0
        cumulsum[i][i] = arr[i]

    for l in range(1, len(arr)):
        for i in range(len(arr) - l):
            cumulsum[i][i + l] = cumulsum[i][i + l - 1] + arr[i + l]
            for k in range(i, i + l):
                dp[i][i + l] = min(
                    dp[i][i + l],
                    dp[i][k] + dp[k + 1][i + l] + cumulsum[i][i + l]
                )

    print(dp[0][-1])
