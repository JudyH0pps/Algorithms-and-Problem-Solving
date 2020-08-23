from collections import deque

delta = (
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1)
)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    visit = [[float('inf')] * N for _ in range(N)]
    visit[0][0] = 0
    def bfs():
        q = deque()
        q.append((0, 0))
        while q:
            row, col = q.popleft()
            if row == N - 1 and col == N - 1:
                continue
            for dr, dc in delta:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < N and 0 <= nc < N and visit[row][col] + board[nr][nc] < visit[nr][nc]:
                    visit[nr][nc] = visit[row][col] + board[nr][nc]
                    q.append((nr, nc))
        return visit[N-1][N-1]

    print('#%d' % tc, bfs())
