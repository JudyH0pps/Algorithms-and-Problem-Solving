import sys

input = lambda: sys.stdin.readline().rstrip()
f = open('input.txt', 'r')
input = lambda: f.readline().rstrip()

from collections import defaultdict

N, M = map(int, input().split())

graph = defaultdict(list)
length = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for c in range(2, N - 2):
    pass
