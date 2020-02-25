# ﻿1261 알고스팟

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

M, N = map(int, input().split())
if (M,N) == (1,1):
    print(0)
board = [list(map(int, input())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]

delta = (
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1)
    )

def findEXIT():
    nextq = deque()
    visit[0][0] = 1
    nextq.append((0, 0))
    kabe = 0
    while nextq:
        kabe += 1
        q = nextq
        nextq = deque()
        while q:
            row, col = q.popleft()
            for i in range(4):
                dr, dc = delta[i]
                nr = row + dr
                nc = col + dc
                if 0 <= nr < N and 0 <= nc < M and not visit[nr][nc]:
                    if (nr,nc) == (N-1,M-1):
                        print(kabe-1)
                        return
                    visit[nr][nc] = 1
                    if board[nr][nc]:
                        nextq.append((nr,nc))
                        continue
                    q.append((nr,nc))

if not (M,N) == (1,1):
    findEXIT()
