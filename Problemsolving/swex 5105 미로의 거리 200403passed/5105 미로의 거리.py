from collections import deque

delta = ((0, 1), (1, 0), (-1, 0), (0, -1))


def iswall(row, col):
    if 0 <= row < N and 0 <= col < N:
        return False
    return True


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]

    def find_start():
        for r in range(N):
            for c in range(N):
                if board[r][c] == 2:
                    return r, c

    startr, startc = find_start()

    def BFS(startr, startc):
        q = deque()
        q.append((startr, startc, 0))
        while q:
            row, col, level = q.popleft()
            for dr, dc in delta:
                nr = row + dr
                nc = col + dc
                if iswall(nr, nc) or (board[nr][nc] != 3 and board[nr][nc]):
                    continue
                if board[nr][nc] == 3:
                    return level
                board[nr][nc] = 1
                q.append((nr, nc, level + 1))
        return 0

    print("#%d" % tc, BFS(startr, startc))
