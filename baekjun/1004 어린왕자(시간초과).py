import sys

input = lambda:sys.stdin.readline().rstrip()
# f = open('input1004.txt', 'r')
# input = lambda: f.readline().rstrip()

T = int(input())

for tc in range(T):
    sx, sy, ex, ey = map(int, input().split())
    sp = -1
    spnum = 0
    ep = -1
    epnum = 0
    sr = float('inf')
    er = float('inf')
    n = int(input())
    planets = []
    parent = [-1] * n

    for _ in range(n):
        planets.append(tuple(map(int, input().split())))

    for i in range(n):
        ax, ay, ar = planets[i]
        dist = ((ax - sx) ** 2 + (ay - sy) ** 2) ** 0.5
        if ar > dist:
            spnum += 1
            if sr > ar:
                sp = i
                sr = ar

        dist = ((ax - ex) ** 2 + (ay - ey) ** 2) ** 0.5
        if ar > dist:
            epnum += 1
            if er > ar:
                ep = i
                er = ar

        for j in range(i + 1, n):
            bx, by, br = planets[j]
            dist = ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5
            sum_of_r = abs(ar - br)
            if dist < sum_of_r:
                if ar > br and (parent[j] == -1 or planets[parent[j]][2] > ar):
                    parent[j] = i
                elif ar < br and (parent[i] == -1 or planets[parent[i]][2] > br):
                    parent[i] = j

    more = sp
    less = ep
    if spnum < epnum:
        more = ep
        less = sp

    cnt = abs(spnum - epnum)
    # print('--')
    # print(sp, ep)
    # print(spnum, epnum)
    # print(parent)
    # print(cnt)
    # print('--')
    for _ in range(abs(spnum - epnum)):
        ep = parent[ep]

    while sp != ep:
        cnt += 2
        sp = parent[sp]
        ep = parent[ep]

    print(cnt)