#5248 그룹 나누기
T = int(input())


def findP(x):
    if parent[x] == x:
        return x
    p = findP(parent[x])
    parent[x] = p
    return p


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pair = tuple(map(int, input().split()))
    parent = [x for x in range(N)]

    for i in range(0, len(pair), 2):
        a, b = pair[i] - 1, pair[i + 1] - 1
        ap = findP(a)
        bp = findP(b)
        if ap <= bp:
            parent[bp] = ap
        else:
            parent[ap] = bp

    # print([x + 1 for x in range(N)])
    # print(parent)

    group = set()
    cnt = 0
    for x in parent:
        x = findP(x)
        if x not in group:
            group.add(x)
            cnt += 1

    print('#%d' % tc, cnt)
