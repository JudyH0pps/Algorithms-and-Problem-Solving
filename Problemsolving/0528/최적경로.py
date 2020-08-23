T = int(input())


def dfs(before, level, score):
    global min_l

    if level == len(nums):
        if min_l > score + graph[before][1]:
            min_l = score + graph[before][1]
        return

    for n in nums:
        if not visit[n] and score + graph[before][n] < min_l:
            visit[n] = 1
            dfs(n, level + 1, score + graph[before][n])
            visit[n] = 0


for tc in range(1, T + 1):
    N = int(input())
    xys = tuple(map(int, input().split()))

    graph = [[0] * (N + 2) for _ in range(N + 2)]
    dot = []

    for i in range(0, len(xys), 2):
        x, y = xys[i], xys[i + 1]
        dot.append((x, y))

    for i in range(len(dot)):
        x1, y1 = dot[i]
        for j in range(i + 1, len(dot)):
            x2, y2 = dot[j]
            length = abs(x1 - x2) + abs(y1 - y2)
            graph[i][j] = length
            graph[j][i] = length

    min_l = float('inf')
    nums = list(range(2, N + 2))
    visit = [0] * (N + 2)

    dfs(0, 0, 0)

    print('#%d' % tc, min_l)
