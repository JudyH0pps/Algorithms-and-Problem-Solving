import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 4 + 1)

itoc = {}


def ctoi(c):
    if ord(c) >= ord('a'):
        itoc[ord(c) - ord('a') + 26] = c
        return ord(c) - ord('a') + 26
    itoc[ord(c) - ord('A')] = c
    return ord(c) - ord('A')


def dfs(top, node):
    for child in graph[node]:
        if visit[child]:
            continue
        answer.append([top, child])
        visit[child] = 1
        dfs(top, child)


graph = [[] for _ in range(52)]
N = int(input())

for _ in range(N):
    a, b = input().split(' => ')
    graph[ctoi(a)].append(ctoi(b))

answer = []
for i in range(52):
    if graph[i]:
        visit = [0] * 52
        visit[i] = 1
        dfs(i, i)

answer.sort()
print(len(answer))
for p, q in answer:
    print(itoc[p], '=>', itoc[q])
