import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 4 + 1)


def dfs(node):
    dp[0][node] = 0
    dp[1][node] = vills[node]
    for nextNode in graph[node]:
        if visit[nextNode]:
            continue
        visit[nextNode] = 1
        dfs(nextNode)
        dp[0][node] += max(dp[0][nextNode], dp[1][nextNode])
        dp[1][node] += dp[0][nextNode]


N = int(input())
vills = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0] * (N + 1) for _ in range(2)]

visit = [0] * (N + 1)
visit[1] = 1
dfs(1)
print(max(dp[1][1], dp[0][1]))
