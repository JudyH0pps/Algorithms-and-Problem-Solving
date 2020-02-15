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
from copy import deepcopy
from collections import defaultdict


# . 빈 칸, # 벽 이동불가, a~f 열쇠 , A~F문(열쇠 있어야만 이동가능),0 현재 위치, 1출구
def printB(pan):
    for i in range(N):
        for j in range(M):
            print(pan[i][j], end=' ')
        print()


def isWall(row, col):
    if 0 <= row < N and 0 <= col < M:
        return False
    return True


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def BFS(level, row, col, objects, chk):
    q = deque()
    q.append((level, row, col))
    while q:
        level, row, col = q.popleft()
        chk[row][col] = 1
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if isWall(nr, nc):
                continue
            next = board[nr][nc]
            if next == '#' or chk[nr][nc] or 65 <= ord(next) <= 70:
                continue
            if next == '1' or 97 <= ord(next) <= 102:
                if (level + 1, next, nr, nc) not in objects:
                    objects.append((level + 1, next, nr, nc))
            q.append((level + 1, nr, nc))
    return objects


doors = defaultdict(list)
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
for r in range(N):
    for c in range(M):
        now = board[r][c]
        if now == '0':
            board[r][c] = '.'
            start = (r, c)
        elif 65 <= ord(now) <= 70:
            doors[now].append((r, c))

minTime = 1000000
find = False


def DFS(r, c, time, objects):
    chk = [[0] * M for _ in range(N)]
    objects = BFS(0, r, c, objects, chk)
    if not objects:
        return
    n = 0
    for distance, obj, nr, nc in objects:
        nobjects = deepcopy(objects)
        nobjects.pop(n)
        n += 1
        if obj == '1':
            global minTime, find
            minTime = min(minTime, time + distance)
            find = True
            continue
        obj = obj.upper()
        tmps = []
        tmps.append((nr, nc, board[nr][nc]))
        board[nr][nc] = '.'
        for dr, dc in doors[obj]:
            tmps.append((dr, dc, board[dr][dc]))
            board[dr][dc] = '.'
        DFS(nr, nc, time + distance, nobjects)
        for tr, tc, val in tmps:
            board[tr][tc] = val


DFS(*start, 0, [])

if find:
    print(minTime)
else:
    print(-1)
