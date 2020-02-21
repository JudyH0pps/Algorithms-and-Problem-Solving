# ﻿2573 빙산

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt", "r")
    input = lambda: f.readline().rstrip()
else:
    import sys

    input = lambda: sys.stdin.readline().rstrip()

################################
from collections import deque


def printB(board):
    for i in range(N):
        for j in range(M):
            print('%2d' % board[i][j], end=' ')
        print()
    print()


delta = (
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
)


def BFS(row, col):
    q = deque()
    q.append((row, col))
    while q:

        row, col = q.pop()
        visit[row][col] = 1

        for i in range(4):
            dr, dc = delta[i]
            nr = row + dr
            nc = col + dc
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc]>0 and not visit[nr][nc]:
                q.append((nr, nc))


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

for r in range(N):
    for c in range(M):
        if not board[r][c]:
            board[r][c] = -1

time = 0
island = -1
while island < 2:
    time += 1

    for r in range(N):
        for c in range(M):
            if board[r][c] != -1:
                cnt = 0
                for i in range(4):
                    dr, dc = delta[i]
                    nr = r + dr;
                    nc = c + dc
                    if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == -1:
                        cnt += 1
                board[r][c] = max(0, board[r][c] - cnt)

    island = 0
    visit = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if not visit[r][c] and board[r][c] > 0:
                BFS(r, c)
                island += 1
            elif board[r][c] == 0:
                board[r][c] = -1
    if island == 0:
        print(0)
        break
else:
    print(time)
