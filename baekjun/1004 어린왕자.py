import sys

MODE = 0
if MODE:
    input = lambda: sys.stdin.readline().rstrip()
else:
    f = open('input1004.txt', 'r')
    input = lambda: f.readline().rstrip()

T = int(input())

for tc in range(T):
    sx, sy, ex, ey = map(int, input().split())
    sp = []
    ep = []
    n = int(input())
    planets = []
    parent = [-1] * n

    for _ in range(n):
        planets.append(tuple(map(int, input().split())))

    for i in range(n):
        ax, ay, ar = planets[i]
        dist = ((ax - sx) ** 2 + (ay - sy) ** 2) ** 0.5
        if ar > dist:
            sp.append((ar, i))

        dist = ((ax - ex) ** 2 + (ay - ey) ** 2) ** 0.5
        if ar > dist:
            ep.append((ar, i))

    sp.sort(key=lambda x: -x[0])
    ep.sort(key=lambda x: -x[0])
    sp = list(map(lambda x: x[1], sp))
    ep = list(map(lambda x: x[1], ep))

    i = 0
    while i < min(len(sp), len(ep)) and sp[i] == ep[i]:
        i += 1

    print(len(sp) + len(ep) - 2 * i)
