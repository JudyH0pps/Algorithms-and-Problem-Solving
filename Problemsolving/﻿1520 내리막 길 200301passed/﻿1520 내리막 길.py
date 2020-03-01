# ﻿1520 내리막 길

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
delta = ((0, 1), (1, 0), (-1, 0), (0, -1))


def DFS(row, col):
    now = board[row][col]
    visit[row][col] = 0
    for dr, dc in delta:
        nr = row + dr
        nc = col + dc
        if 0 <= nr < N and 0 <= nc < M and now < board[nr][nc]:
            if visit[nr][nc] != -1:
                visit[row][col] += visit[nr][nc]
            else:
                visit[row][col] += DFS(nr, nc)
    return visit[row][col]


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[-1] * M for _ in range(N)]
visit[0][0] = 1
print(DFS(N - 1, M - 1))
