import sys

input = lambda: sys.stdin.readline().rstrip()
# f = open('input.txt', 'r')
# input = lambda: f.readline().rstrip()


def recur(r, c, rs, cs, time):
    if time == 0:
        return 0

    l = N ** time
    unit = l // N
    ro = N - 1
    co = N - 1
    for rp in range(rs + l - unit, rs - 1, -unit):
        for cp in range(cs + l - unit, cs - 1, -unit):
            if rp <= r and cp <= c:
                break
            co -= 1
        else:
            co = N - 1
            ro -= 1
            continue
        break
    # print(rp, cp, '->', r, c)
    # print(ro, co)

    blackspot = range(N // 2 - K // 2, N // 2 + (K - 1) // 2 + 1)
    if ro in blackspot and co in blackspot:
        return 1

    return recur(r, c, rp, cp, time - 1)


s, N, K, R1, R2, C1, C2 = map(int, input().split())

board = [[0] * (C2 - C1 + 1) for _ in range(R2 - R1 + 1)]

for r in range(R1, R2 + 1):
    for c in range(C1, C2 + 1):
        board[r - R1][c - C1] = recur(r, c, 0, 0, s)

for line in board:
    for dot in line:
        print(dot, end='')
    print()
