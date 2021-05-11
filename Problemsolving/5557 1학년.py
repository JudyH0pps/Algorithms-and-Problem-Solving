import sys
sys.stdin = open('input.txt')

answer = 0
N = int(input())
nums = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N - 1)]

dp[0][nums[0]] = 1

for i in range(1, N - 1):
    for j in range(21):
        if j + nums[i] <= 20:
            dp[i][j + nums[i]] += dp[i - 1][j]
        if j - nums[i] >= 0:
            dp[i][j - nums[i]] += dp[i - 1][j]

print(dp[-1][nums[-1]])
