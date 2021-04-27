import sys
sys.stdin = open('input.txt')


delta = ((0, 1), (1, 0), (-1, 0), (0, -1))


def counterClock(board):
    R = len(board)
    C = len(board[0])
    nextBoard = [[0] * R for _ in range(C)]
    for r in range(R):
        for c in range(C):
            nextBoard[C - c - 1][r] = board[r][c]
    return nextBoard


def gravity(board):
    for c in range(N):
        stack = []
        for r in range(N):
            if board[r][c] == -1:
                cnt = 1
                while stack:
                    board[r - cnt][c] = stack.pop()
                    cnt += 1
            elif board[r][c] != -2:
                stack.append(board[r][c])
                board[r][c] = -2
        cnt = 1
        while stack:
            board[N - cnt][c] = stack.pop()
            cnt += 1
    return board


def DFS(r, c, color):
    visit[r][c] = 1
    global cnt, rainbowCnt
    cnt += 1
    if board[r][c] == 0:
        rainbowCnt += 1
    for dr, dc in delta:
        nr = r + dr
        nc = c + dc
        if not (0 <= nr < N and 0 <= nc < N) or (nr, nc) in group:
            continue
        if board[nr][nc] not in (color, 0):
            continue
        group.add((nr, nc))
        DFS(nr, nc, color)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

score = 0

while True:
    visit = [[0] * N for _ in range(N)]
    group = set()
    maxGroup = set()
    maxCnt = -1
    maxRainbow = -1
    maxR = -1
    maxC = -1
    for r in range(N):
        for c in range(N):
            if visit[r][c] or board[r][c] in (0, -1, -2):
                continue
            cnt = 0
            rainbowCnt = 0
            group = set()
            group.add((r, c))
            DFS(r, c, board[r][c])
            if cnt >= 2 and (cnt, rainbowCnt, r, c) > (maxCnt, maxRainbow, maxR, maxC):
                maxGroup = group
                maxCnt = cnt
                maxRainbow = rainbowCnt
                maxR = r
                maxC = c

    if len(maxGroup) == 0:
        break
    score += len(maxGroup) ** 2
    for r, c in maxGroup:
        board[r][c] = -2
    board = gravity(counterClock(gravity(board)))

print(score)
