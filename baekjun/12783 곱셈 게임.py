import sys

input = lambda: sys.stdin.readline().rstrip()
# f = open('input.txt', 'r')
# input = lambda: f.readline().rstrip()


def findminx(n):
    if n in dp:
        return dp[n]

    for c in str(n):
        if c not in kinds:
            break
    else:
        dp[n] = 0
        return 0

    minx = 1000000
    for k in range(2, int(round(n ** 0.5, 100)) + 1):
        if n % k == 0:
            x = findminx(k) + findminx(n // k) + 1
            if x < minx:
                minx = x
    dp[n] = minx
    return minx


T = int(input())
for tc in range(T):
    kinds = tuple(input().split())[1:]
    M = int(input())
    dp = dict()
    for i in kinds:
        dp[int(i)] = 0
    # print(dp)
    for _ in range(M):
        n = int(input())
        x = findminx(n)
        if x == 1000000:
            x = -1
        print(x)