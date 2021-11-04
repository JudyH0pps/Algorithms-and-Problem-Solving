import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

# f = open("input.txt", "r")
# input = lambda: f.readline().rstrip()

N, M = map(int, input().split())
L = int(input())

walls = [list(map(int, input().split())) for _ in range(L)]
graph = defaultdict(list)
cnt = defaultdict(int)

S = N * M

delta = (-M, 1, M, -1)

for n in range(1, S + 1):
    for d in delta:
        if 0 < n + d <= S and not (n % M == 0 and d == 1 or n % M == 1 and d == -1):
            graph[n].append(n + d)
            cnt[n] += 1

for a, b in walls:
    cnt[a] -= 1
    cnt[b] -= 1
    graph[a].remove(b)
    graph[b].remove(a)

fix = []

for n, c in cnt.items():
    if c == 1:
        fix.append(n)

while True:
    while fix:
        node = fix.pop()
        if cnt[node] <= 0:
            continue
        pair = graph[node][0]
        cnt[node] = 0
        cnt[pair] = 0
        graph[pair].remove(node)
        graph[node].remove(pair)

        print(node, pair)

        for n in graph[pair]:
            graph[n].remove(pair)
            cnt[n] -= 1
            if cnt[n] == 1:
                fix.append(n)

    for p in range(1, S + 1):
        if cnt[p] > 0:
            break
    else:
        break

    pair = graph[p][0]
    print(p, pair)

    cnt[p] = cnt[pair] = 0
    graph[p].remove(pair)
    graph[pair].remove(p)

    for n in graph[p]:
        graph[n].remove(p)
        cnt[n] -= 1
        if cnt[n] == 1:
            fix.append(n)

    for n in graph[pair]:
        graph[n].remove(pair)
        cnt[n] -= 1
        if cnt[n] == 1:
            fix.append(n)
