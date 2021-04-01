import sys
sys.setrecursionlimit(6001)

sys.stdin = open('input.txt', 'r')


# def input(): return sys.stdin.readline()


def C(x, y):
    if dp[x][y]:
        return dp[x][y]
    if x == 0:
        return 1
    if y == 1:
        return x
    dp[x][y] = C(x - 1, y) * C(x - 1, y - 1)
    dp[x][y] %= 1000000007
    print(dp[x][y])
    return dp[x][y] % 1000000007


T = int(input())

for _ in range(T):
    print('##', _)
    L = int(input())
    if L % 2:
        print(0)
        continue
    dp = [[0] * (L + 1) for _ in range(L + 1)]
    print(C(L - 2, L // 2 - 1))

print(dp)
