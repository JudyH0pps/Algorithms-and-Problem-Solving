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

def BFS(level, row, col, board, objects):
    q = deque()
    q.append((level,row,col))
    while q:
        level, row, col = q.popleft()
        board[row][col] = '#'
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if isWall(nr, nc):
                continue
            next = board[nr][nc]
            if next == '#' or 65 <= ord(next) <= 70:
                continue
            if next == '1' or 97 <= ord(next) <= 102:
                objects.append((level + 1, next, nr, nc))
            q.append((level+1,nr,nc))
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

q = deque()
q.append(start + (0, []))
minTime = 1000000
find = False
while q:
    r, c, time, path = q.popleft()
    now = deepcopy(board)
    for delr, delc in path:
        now[delr][delc] = '.'
    # printB(now)
    objects = BFS(0, r, c, now, objects=[])
    # print(objects)
    # print(path)
    # print()
    if not objects:
        continue
    for distance, obj, nr, nc in objects:
        if obj == '1':
            minTime = min(minTime, time + distance)
            find = True
            continue
        obj = obj.upper()
        npath = deepcopy(path)
        npath.append((nr, nc))
        for delr, delc in doors[obj]:
            npath.append((delr, delc))
        q.append((nr, nc, time + distance, npath))

def DFS(start,)
if find:
    print(minTime)
else:
    print(-1)
