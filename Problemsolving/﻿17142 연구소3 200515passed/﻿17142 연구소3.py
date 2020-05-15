# ﻿17142 연구소3

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
from copy import deepcopy


def printB(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()
    print()


def choose(level, last):
    if level == M:
        splice(chosen)
        return
    for i in range(last, len(virus)):
        chosen.append(i)
        choose(level + 1, i + 1)
        chosen.pop()


delta = (
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1)
)


def boardchk(cboard):
    for r in range(N):
        for c in range(N):
            if cboard[r][c] == 0:
                return False
    return True


def splice(chosen):
    cboard = deepcopy(board)

    q = deque()
    for i in chosen:
        r, c = virus[i]
        cboard[r][c] = '@'
        q.append((r, c, 0))

    max_level = 0

    # initq = deepcopy(q)

    global min_step

    while q:
        r, c, level = q.popleft()
        if level > min_step:
            return
        for dr, dc in delta:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < N and 0 <= nc < N and (cboard[nr][nc] == 0 or cboard[nr][nc] == -1):
                if board[nr][nc] == -1 and boardchk(cboard):
                    max_level = max(level, max_level)
                    if min_step > max_level:
                        min_step = max_level
                        # printB(cboard)
                        # print(initq)
                        # print(max_level)
                        return
                cboard[nr][nc] = level + 1
                max_level = max(max_level, level + 1)
                q.append((nr, nc, level + 1))

    if boardchk(cboard) and min_step > max_level:
        min_step = max_level
        # printB(cboard)
        # print(initq)
        # print(max_level)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
virus = []
for r in range(N):
    for c in range(N):
        if board[r][c] == 2:
            virus.append((r, c))
            board[r][c] = -1
        elif board[r][c] == 1:
            board[r][c] = '■'

chosen = []
min_step = float('inf')
choose(0, 0)

if min_step == float('inf'):
    print(-1)
else:
    print(min_step)
