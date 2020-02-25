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
sunvisit = [[0] * n for _ in range(n)]
moonvisit = [[0] * n for _ in range(n)]

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def gogo():
    q = deque()
    q.append((0, 0, 0))
    sunvisit[0][0] = 1
    while q:
        row, col, level = q.popleft()

        if ((level + 1) % (2 * m)) < m:
            day = 'sun'
            Night = False
        else:
            day = 'moon'
            Night = True
        # print(row,col,level,Night)
        for i in range(4):
            dr, dc = delta[i]
            nr = row + dr
            nc = col + dc
            if Night:
                visit = moonvisit
            else:
                visit = sunvisit
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
                    if not visit[nr][nc]:
                        flag = True
            else:
                if board[nr][nc]:
                    continue
            if (nr, nc) == (n - 1, n - 1):
                # print(level+1,nr,nc)
                print((level + 1) // (2 * m) + 1, day)
                return True

            if flag:
                visit[nr][nc] = level + 2
                q.append((nr, nc, level + 1))


if not gogo():
    print(-1)

# for _ in moonvisit:
#     print(_)
# print()
# for _ in sunvisit:
#     print(_)
# print()
