# ﻿1194 달이 차오른다 가자

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


# . 빈 칸, # 벽 이동불가, a~f 열쇠 , A~F문(열쇠 있어야만 이동가능),0 현재 위치, 1출구
def printB(pan):
    for i in range(N):
        for j in range(M):
            print(pan[i][j], end=' ')
        print()
    print()


def isWall(row, col):
    if 0 <= row < N and 0 <= col < M:
        return False
    return True


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

keydic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}


def chk(char, keys):
    char = char.upper()
    return keys & (1 << keydic[char])


def BFS(row, col):
    q = deque()
    q.append((1, 1, row, col, 0))
    while q:
        level, keylevel, row, col, keys = q.popleft()
        # print(lastkey)
        printB(visit)

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if isWall(nr, nc) or board[nr][nc] == '#' or (visit[nr][nc] and visit[nr][nc] < keylevel):
                continue
            visit[nr][nc] = keylevel + 1
            if board[nr][nc] == '1':
                return level
            elif board[nr][nc] == '.' or chk(board[nr][nc], keys):
                q.append((level + 1, keylevel + 1, nr, nc, keys))
            elif 97 <= ord(board[nr][nc]) <= 102:
                nlkey = keydic[board[nr][nc].upper()]
                q.append((level + 1, 1, nr, nc, keys | (1 << nlkey)))
    return -1


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visit = [[0] * M for _ in range(N)]


def findStart():
    for r in range(N):
        for c in range(M):
            now = board[r][c]
            if now == '0':
                board[r][c] = '.'
                return r, c


r, c = findStart()
visit[r][c] = 1
print(BFS(r, c))
