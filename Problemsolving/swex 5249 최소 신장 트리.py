import sys

sys.stdin = open('5249.txt')

#5249 최소 신장 트리
import heapq

T = int(input())


def min_edge():
    w, i, j = heapq.heappop(edges)
    return w, i, j


def findP(x):
    if parent[x] == x:
        return x
    p = findP(parent[x])
    parent[x] = p
    return p


def union_chk():
    t = findP(parent[0])
    for x in parent[1:]:
        if findP(x) != t:
            return False
    return True


for tc in range(1, T + 1):
    V, E = map(int, input().split())
    parent = [x for x in range(V + 1)]
    edges = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        if n2 <= n1:
            n1, n2 = n2, n1
        heapq.heappush(edges, (w, n1, n2))

    w_sum = 0

    while not union_chk():
        while True:
            w, a, b = min_edge()
            ap = findP(a)
            bp = findP(b)
            if ap != bp:
                w_sum += w
                break
        parent[bp] = ap

    print('#%d' % tc, w_sum)
