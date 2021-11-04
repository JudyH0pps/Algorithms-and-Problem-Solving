import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()


# f = open("input.txt", "r")
# input = lambda: f.readline().rstrip()


def toEnd(fuel):
    dp = [0] * (N + 1)

    for i in range(N + 1):
        r, c, add = stops[i]
        dp[i] = fuel - (r + c - 2)

    for i in range(N + 1):
        if dp[i] < 0:
            continue
        ar, ac, afuel = stops[i]
        holding = afuel + dp[i]
        for j in range(i + 1, N + 1):
            br, bc, bfuel = stops[j]
            if ar > br or ac > bc:
                continue
            dist = br - ar + bc - ac
            dp[j] = max(dp[j], holding - dist)
    # print(mid, dp)
    return dp[-1]


R, C = map(int, input().split())
N = int(input())
stops = [list(map(int, input().split())) for _ in range(N)] + [[R, C, 0]]
stops.sort(key=lambda x: x[0] + x[1])

left = 0
right = R + C - 2
minLeftFuel = float('inf')
while left <= right:
    mid = (left + right) // 2
    leftFuel = toEnd(mid)
    if leftFuel >= 0:
        minLeftFuel = min(mid, minLeftFuel)
    if leftFuel == 0:
        break
    elif leftFuel < 0:
        left = mid + 1
    else:
        right = mid - 1

print(minLeftFuel)
