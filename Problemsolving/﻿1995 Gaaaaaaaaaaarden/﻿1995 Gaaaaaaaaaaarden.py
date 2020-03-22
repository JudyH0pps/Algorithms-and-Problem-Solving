# ﻿1995 Gaaaaaaaaaaarden
import sys
from collections import deque

MODE = 1
if MODE:
    f = open("input.txt", "r")
    input = lambda: f.readline().rstrip()
else:
    input = lambda: sys.stdin.readline().rstrip()
##############################

delta = ((0, 1), (1, 0), (-1, 0), (0, -1))


def printB(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print('%2d' % board[i][j], end=' ')
        print()
    print()


def isWall(row, col):
    if 0 <= row < N and 0 <= col < M:
        return False
    return True


def selectred(last, nowR):
    if nowR == R:
        # print(green)
        # print(red)
        # if green == [(11, 0), (11, 11)] and red == [(8, 7), (11, 6), (12, 0), (12, 14)]:
        cntflower()
        return
    for i in range(last + 1, len(land)):
        if visit[i]:
            continue
        red.append(land[i])
        visit[i] ^= 1
        selectred(i, nowR + 1)
        visit[i] ^= 1
        red.pop()


def selectgreen(last, nowG):
    if nowG == G:
        selectred(-1, 0)
        return

    for i in range(last + 1, len(land)):
        if visit[i]:
            continue
        green.append(land[i])
        visit[i] ^= 1
        selectgreen(i, nowG + 1)
        visit[i] ^= 1
        green.pop()


def cntflower():
    greenvisit = [[0] * M for _ in range(N)]
    redvisit = [[0] * M for _ in range(N)]
    greenq = deque(green)
    redq = deque(red)
    for r, c in greenq:
        greenvisit[r][c] = 1
    for r, c in redq:
        redvisit[r][c] = 1
    # print('stttart')
    # print(greenq)
    # print(redq)
    # printB(greenvisit)
    # printB(redvisit)
    flower = 0
    time = 2
    while greenq or redq:
        nextgreenq = len(greenq)
        for _ in range(nextgreenq):
            row, col = greenq.popleft()
            if redvisit[row][col]:
                continue
            for dr, dc in delta:
                nr = row + dr
                nc = col + dc
                if isWall(nr, nc) or board[nr][nc] == 0 or greenvisit[nr][nc]:
                    continue
                greenvisit[nr][nc] = time
                greenq.append((nr, nc))

        nextredq = len(redq)
        for _ in range(nextredq):
            row, col = redq.popleft()
            for dr, dc in delta:
                nr = row + dr
                nc = col + dc
                if isWall(nr, nc) or board[nr][nc] == 0 or redvisit[nr][nc]:
                    continue
                redvisit[nr][nc] = time
                if greenvisit[nr][nc] == time:
                    redvisit[nr][nc] = -1
                    flower += 1
                else:
                    redq.append((nr, nc))
        time += 1

        # print(greenq)
        # print(redq)
        # printB(greenvisit)
        # printB(redvisit)

    global maxFlower
    if flower > maxFlower:
        # print(flower)
        # print(green)
        # print(red)
        maxFlower = flower


N, M, G, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

land = []

for r in range(N):
    for c in range(M):
        if board[r][c] == 2:
            land.append((r, c))

visit = [0] * len(land)

green = []
red = []
maxFlower = -1
selectgreen(-1, 0)
print(maxFlower)
