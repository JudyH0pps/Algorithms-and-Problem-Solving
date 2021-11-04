import sys

input = lambda: sys.stdin.readline().rstrip()
# f = open('input.txt', 'r')
# input = lambda: f.readline().rstrip()

T = int(input())
for _ in range(T):
    N = int(input())
    cards = list(map(int, input().split()))

    dp = []

    for card in cards:
        dp.append((card, 0))

    for leng in range(2, N + 1):
        nextdp = [0] * N
        for start in range(N - leng + 1):
            end = start + leng
            x1, x2 = dp[start]
            y1, y2 = dp[start + 1]
            if x2 + cards[end - 1] > y2 + cards[start]:
                M = x2 + cards[end - 1]
                m = x1
            else:
                M = y2 + cards[start]
                m = y1
            nextdp[start] = (M, m)
        dp = nextdp

    # print(dp)
    print(dp[0][0])
