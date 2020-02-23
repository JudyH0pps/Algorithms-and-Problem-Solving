#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt", "r")
    input = lambda: f.readline().rstrip()
else:
    import sys

    input = lambda: sys.stdin.readline().rstrip()
################################

N, M, H = map(int, input().split())

blocks = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (H + 1) for _ in range(N + 1)]

for level in range(1, N + 1):
    for i in range(H + 1):
        if dp[level-1][i]:
            for block in blocks[level - 1]:
                if i + block <= H:
                    dp[level][i + block] += dp[level-1][i]
        dp[level][i] += dp[level - 1][i]
    for block in blocks[level - 1]:
        dp[level][block] += 1

    # print(dp[level])

print(dp[-1][-1] % 10007)
