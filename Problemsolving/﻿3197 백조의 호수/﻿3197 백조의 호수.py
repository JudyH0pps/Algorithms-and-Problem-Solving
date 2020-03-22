# ﻿3197 백조의 호수

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
from itertools import product
from collections import deque


def printB(board):
    for i in range(N):
        for j in range(M):
            print("%2s" % board[i][j], end=' ')
        print()
    print()


delta = ((0, 1), (1, 0), (-1, 0), (0, -1))


def isWall(r, c):
    if 0 <= r < N and 0 <= c < M:
        return False
    return True


def firstbfs(row, col, i):
    q = deque()
    q.append((row, col))
    visit[i][row][col] = 0
    icevisit[row][col] = 1
    while q:
        row, col = q.popleft()

        for dr, dc in delta:
            nr = row + dr
            nc = col + dc
            if isWall(nr, nc) or icevisit[nr][nc]:
                continue
            if board[nr][nc] == 'L':
                return True
            elif board[nr][nc] == 'X':
                iceq.append((nr, nc))
                swanq[0].append((nr, nc))
                visit[i][nr][nc] = 1
                icevisit[nr][nc] = 1
                continue
            else:
                icevisit[nr][nc] = 1
                visit[i][nr][nc] = 0
                q.append((nr, nc))
    return False


def BFS(row, col):
    q = deque()
    q.append((row, col))
    icevisit[row][col] = 1
    while q:
        row, col = q.popleft()

        for dr, dc in delta:
            nr = row + dr
            nc = col + dc
            if isWall(nr, nc) or icevisit[nr][nc]:
                continue
            elif board[nr][nc] == 'X':
                icevisit[nr][nc] = 1
                iceq.append((nr, nc))
                continue
            else:
                icevisit[nr][nc] = 1
                q.append((nr, nc))


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
icevisit = [[0] * M for _ in range(N)]
visit = [[[-1] * M for _ in range(N)] for _ in range(2)]

swanq = [deque()]*2
iceq = deque()

swan = [0, 0]
i = 0
find = False
for r, c in product(range(N), range(M)):
    if board[r][c] == 'L':
        swan[i] = (r, c)
        board[r][c] = '.'
        if firstbfs(r, c, i):
            find = True
            break
        if i == 1:
            break
        i += 1

if find:
    print(0)
else:
    for r in range(N):
        for c in range(M):
            if board[r][c] == '.':
                BFS(r, c)

    printB(board)
    printB(visit[0])
    printB(visit[1])

    while iceq:
        level = 1
        nexttime = len(iceq)
        for _ in range(nexttime):
            icer, icec = iceq.popleft()
            board[icer][icec] = '.'
            for dr, dc in delta:
                nir = icer + dr
                nic = icec + dc
                if isWall(nir, nic) or icevisit[nir][nic]:
                    continue
                icevisit[nir][nic] = 1
                iceq.append((nir, nic))

        printB(board)
        for i in range(2):
            nextq = deque()
            while swanq[i]:
                r, c = swanq[i].popleft()
                




