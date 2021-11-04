import sys

input = lambda: sys.stdin.readline().rstrip()
# f = open('input1753.txt', 'r')
# input = lambda: f.readline().rstrip()

from collections import defaultdict
import heapq

V, E = map(int, input().split())
K = int(input())
K -= 1
graph = defaultdict(list)
dist = [float('inf')] * V
visit = [0] * V
for _ in range(E):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, w))

s = K
dist[s] = 0
edges = [(0, s)]
while edges:
    w, s = heapq.heappop(edges)
    if visit[s]:
        continue
    visit[s] = 1

    for v, w in graph[s]:
        if visit[v]:
            continue
        dist[v] = min(dist[v], dist[s] + w)
        heapq.heappush(edges, (dist[v], v))

for _ in dist:
    if _ == float('inf'):
        print('INF')
    else:
        print(_)