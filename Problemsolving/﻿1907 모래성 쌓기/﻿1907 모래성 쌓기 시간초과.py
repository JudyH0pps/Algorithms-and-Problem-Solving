# ﻿1907 모래성 쌓기

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
def printB(board):
    for line in board:
        print(line)
    print()


delta = ((0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1))
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    near = [[0] * M for _ in range(N)]

    for r in range(N):
        for c in range(M):
            if board[r][c] == '.':
                for dr, dc in delta:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < N and 0 <= nc < M:
                        near[nr][nc] += 1

    wave = 0
    nextloof = True
    while nextloof:
        # printB(board)
        nextloof = False
        tmp = [[0] * M for _ in range(N)]
        for r in range(1, N - 1):
            for c in range(1, M - 1):
                if board[r][c] != '9' and board[r][c] != '.':
                    if int(board[r][c]) <= near[r][c]:
                        nextloof = True
                        board[r][c] = '.'
                        for dr, dc in delta:
                            nr = r + dr
                            nc = c + dc
                            if 0 <= nr < N and 0 <= nc < M:
                                tmp[nr][nc] += 1

        for r in range(1, N - 1):
            for c in range(1, M - 1):
                near[r][c] += tmp[r][c]

        # printB(near)
        wave += 1

    print('#%d' % test_case, wave - 1)
