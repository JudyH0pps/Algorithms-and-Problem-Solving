#최소합
T = int(input())

delta = (
    (0, 1),
    (1, 0),
)


def DFS(row, col, cumul_sum):
    if row == N - 1 and col == N - 1:
        global min_sum
        min_sum = cumul_sum
        return

    for dr, dc in delta:
        nr = row + dr
        nc = col + dc
        if 0 <= nr < N and 0 <= nc < N:
            if cumul_sum + board[nr][nc] < min_sum:
                DFS(nr, nc, cumul_sum + board[nr][nc])


for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 1690
    DFS(0, 0, board[0][0])
    print('#%d' % tc, min_sum)
