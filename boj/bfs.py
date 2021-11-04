from collections import defaultdict

delta = [
    [1, 2], [1, -2], [-1, 2], [-1, -2],
    [2, 1], [2, -1], [-2, 1], [-2, -1]
]


def dfs(level, r, c):

    if level == 2:
        print(r, c)
        return

    for dr, dc in delta:
        nr = r + dr
        nc = c + dc
        if nr and nc and not visit[nr, nc]:
            visit[nr, nc] = 1
            dfs(level + 1, nr, nc)


visit = defaultdict(int)
dfs(0, 0, 0)
