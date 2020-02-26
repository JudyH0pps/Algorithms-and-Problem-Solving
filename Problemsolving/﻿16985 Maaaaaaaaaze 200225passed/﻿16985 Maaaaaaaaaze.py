# ﻿16985 Maaaaaaaaaze

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0
if not INPUTMODE:
    f = open("input.txt", "r")
    input = f.readline
else:
    import sys

    input = sys.stdin.readline
################################
from copy import deepcopy
from collections import deque

# row,col,h
delta = (
    (0, 0, 1),
    (0, 0, -1),
    (1, 0, 0),
    (0, 1, 0),
    (-1, 0, 0),
    (0, -1, 0)
)


def BFS():
    visit = [[[0]*5 for _ in range(5)] for _ in range(5)]
    if cube[0][0][0] == 0:
        return 126
    visit[0][0][0] = 1
    q = deque()
    q.append((0, 0, 0, 0))
    while q:
        # print('inq')
        row, col, h, level = q.popleft()
        for i in range(6):
            dr, dc, dh = delta[i]
            nr = row + dr
            nc = col + dc
            nh = h + dh
            if 0 <= nr < 5 and 0 <= nc < 5 and 0 <= nh < 5 and cube[nh][nr][nc] and not visit[nh][nr][nc]:
                if (nh, nr, nc) == (4, 4, 4):
                    return level + 1
                visit[nh][nr][nc] = 1
                q.append((nr, nc, nh, level + 1))
    return 126


def clockwise(board):
    nboard = deepcopy(board)
    for r in range(5):
        for c in range(5):
            nboard[r][c] = board[4 - c][r]
    return nboard


def permutations(level):
    if level == 5:
        global cnt
        cnt += 1
        # print(cnt)
        for a in range(4):
            cube[0] = clockwise(cube[0])
            for b in range(4):
                cube[1] = clockwise(cube[1])
                for c in range(4):
                    cube[2] = clockwise(cube[2])
                    for d in range(4):
                        cube[3] = clockwise(cube[3])
                        for e in range(4):
                            cube[4] = clockwise(cube[4])
                            # print(cnt,'-----',a,b,c,d,e)
                            dist = BFS()
                            global minlevel
                            if minlevel > dist:
                                # print(cnt,a,b,c,d,e,dist)
                                # print(cube)
                                minlevel = dist

    for i in range(level, 5):
        cube[i], cube[level] = cube[level], cube[i]
        permutations(level + 1)
        cube[i], cube[level] = cube[level], cube[i]


cube = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]

cnt = 0
minlevel = 126
permutations(0)
if minlevel == 126:
    print(-1)
else:
    print(minlevel)
