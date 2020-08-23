T = int(input())


def findpath(x, path):
    if x == 0:
        path.append(0)
        return
    path.append(parent[x])
    findpath(parent[x], path)


def findp(x, P):
    if x == P:
        return True
    if x == 0:
        return False
    return findp(parent[x], P)


for tc in range(1, T + 1):
    V, E, a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges = list(map(int, input().split()))

    parent = [x for x in range(V)]
    for i in range(0, E * 2, 2):
        p, c = edges[i], edges[i + 1]
        parent[c - 1] = p - 1
    patha = [a]
    pathb = [b]
    findpath(a, patha)
    findpath(b, pathb)

    patha.reverse()
    pathb.reverse()

    for i in range(min(len(patha), len(pathb))):
        if patha[i] != pathb[i]:
            ansnode = patha[i - 1]
            break

    cnt = 0
    for i in range(V):
        if findp(i, ansnode):
            cnt += 1

    print('#%d' % tc, ansnode + 1, cnt)
