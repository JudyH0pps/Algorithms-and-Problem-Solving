# ﻿18224 미로에 갇힌 건우

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
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
    print()


def isWall(row, col):
    if 0 <= row < n and 0 <= col < n:
        return False
    return True


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * n for _ in range(n)]

q = deque()
q.append((0, 0, 0))

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def gogo():
    while q:
        row, col, level = q.popleft()

        visit[row][col] = 1
        if (row, col) == (n - 1, n - 1):
            if Night:
                s = 'moon'
            else:
                s = 'sun'
            print(level // (2*m) + 1, s)
            return True

        if (level // m) % 2 == 0:
            Night = False
        else:
            Night = True

        for i in range(4):
            dr, dc = delta[i]
            nr = row + dr
            nc = col + dc
            if isWall(nr, nc) or visit[nr][nc]:
                continue

            flag = True
            if Night:
                flag = False
                while board[nr][nc] == 1:
                    nr += dr
                    nc += dc
                    if isWall(nr, nc):
                        break
                else:
                    flag = True
            else:
                if board[nr][nc]:
                    continue
            if flag:
                q.append((nr, nc, level + 1))


if not gogo():
    print(-1)
