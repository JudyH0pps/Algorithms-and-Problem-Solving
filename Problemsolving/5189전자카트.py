#전자카트
T = int(input())

def DFS(now, val, level):
    global min_val
    if level == N - 1 and min_val > val + board[now][0]:
        min_val = val + board[now][0]
    for next in range(N):
        if visit[next]:
            continue
        if val + board[now][next] < min_val:
            visit[next] = 1
            DFS(next, val + board[now][next], level + 1)
            visit[next] = 0


for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    visit[0] = 1
    min_val = 10000
    DFS(0, 0, 0)
    print('#%d' % tc, min_val)
