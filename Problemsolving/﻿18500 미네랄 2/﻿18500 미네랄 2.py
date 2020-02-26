# ﻿18500 미네랄 2

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
    for r in range(R):
        for c in range(C):
            print(board[r][c], end='')
        print()
    print()


def isWall(row, col):
    if 0 <= row < R and 0 <= col < C:
        return False
    return True


delta = ((0, 1), (1, 0), (-1, 0), (0, -1))


def BFS(row, col):
    colbot = [0] * C
    visit = [[0] * C for _ in range(R)]
    visit[row][col] = 1
    bottom, left, right = -1, C, -1
    q = deque()
    q.append((row, col))
    while q:
        row, col = q.popleft()
        colbot[col] = max(row, colbot[col])
        bottom = max(bottom, row)
        left = min(left, col)
        right = max(right, col)
        for i in range(4):
            dr, dc = delta[i]
            nr = row + dr
            nc = col + dc
            if not isWall(nr, nc) and board[nr][nc] == 'x' and not visit[nr][nc]:
                visit[nr][nc] = 1
                q.append((nr, nc))

    return bottom, left, right, colbot


arrow = (1, -1)  # 0 동, 1 서


def fall(left, right, bottom, dist, colbot):
    for c in range(left, right + 1):
        q = deque()
        for r in range(colbot[c] + 1):
            q.append(board[r][c])
            board[r][c] = '.'
        for r in range(dist, colbot[c] + 1 + dist):
            board[r][c] = q.popleft()


def shoot(row, direction):
    if direction:
        col = C - 1
    else:
        col = 0

    dc = arrow[direction]

    while not isWall(row, col) and board[row][col] == '.':
        col += dc
    if not isWall(row, col):
        board[row][col] = '.'
        for dr, dc in delta:
            nr = row + dr
            nc = col + dc
            if not isWall(nr, nc) and board[nr][nc] == 'x':
                bottom, left, right, colbot = BFS(nr, nc)
                if bottom < R - 1:

                    mindist = R
                    for c in range(left, right + 1):
                        r = colbot[c] + 1
                        dist = 1
                        while r + dist < R and board[r + dist][c] == '.':
                            dist += 1
                        # print(dist)
                        mindist = min(mindist, dist)
                    # print(colbot,mindist)
                    fall(left, right, bottom, mindist, colbot)
                    break


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
int(input())
right = 0
for H in map(int, input().split()):
    shoot(R - H, right)
    # print(H)
    # printB(board)
    right ^= 1

printB(board)
