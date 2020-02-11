# ﻿17822 원판 돌리기

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
            print(board[i][j], end=' ')
        print()
    print()


dr = [1, 0]
dc = [0, -1]


def isWall(row, col):
    if -1 <= row < N and -1 <= col < M:
        return False
    return True


N, M, T = map(int, input().split())
board = [deque(map(int, input().split())) for _ in range(N)]
bias = [0] * N

for _ in range(T):
    # 0 시계 1 반시계
    x, d, k = map(int, input().split())
    for r in range(x, N + 1, x):
        tmp = bias[r - 1]
        if d == 0:
            bias[r - 1] = (tmp - k) % M
        else:
            bias[r - 1] = (tmp + k) % M

    for i in range(N):
        for _ in range(bias[i]):
            tmp = board[i].popleft()
            board[i].append(tmp)
        bias[i] = 0

    # printB(board)
    summ = 0
    cnt = 0
    dele = False
    delete = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            now = board[r][c]
            if not now:
                continue
            summ += now
            cnt += 1
            for i in range(2):
                nr = r + dr[i]
                nc = c + dc[i]
                if isWall(nr, nc):
                    continue
                next = board[nr][nc]
                if next == now:
                    dele = True
                    delete[r][c] = 1
                    delete[nr][nc] = 1

    if dele:
        for r in range(N):
            for c in range(M):
                if delete[r][c]:
                    board[r][c] = 0
    else:
        if cnt == 0:
            avg = 0
        else:
            avg = summ / cnt
        for r in range(N):
            for c in range(M):
                now = board[r][c]
                if not now:
                    continue
                if now > avg:
                    board[r][c] -= 1
                else:
                    board[r][c] += 1

sub = 0
for r in range(N):
    for c in range(M):
        sub += board[r][c]

print(sub)
