import heapq


def findP(x):
    if x == parents[x]:
        return x
    p = findP(parents[x])
    parents[x] = p
    return p


def union():
    for x in parents[1:]:
        if findP(x) != 0:
            return False
    return True


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    isleX = list(map(int, input().split()))
    isleY = list(map(int, input().split()))

    E = float(input())

    parents = [x for x in range(N)]
    edges = []
    for i in range(N):
        x1, y1 = isleX[i], isleY[i]
        for j in range(i + 1, N):
            x2, y2 = isleX[j], isleY[j]
            dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            heapq.heappush(edges, (dist, i, j))

    w = 0
    while not union():
        dist, a, b = heapq.heappop(edges)
        ap = findP(a)
        bp = findP(b)
        if ap != bp:
            w += E * dist ** 2
            if bp < ap:
                ap, bp = bp, ap
            parents[bp] = ap

    print('#%d' % tc, round(w))
