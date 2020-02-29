# ﻿15683 감시

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
from copy import deepcopy


def printB(board):
    for r in range(N):
        for c in range(M):
            print(board[r][c], end=' ')
        print()
    print()


# 동 남 서 북
delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
arrow = {
    1: (0,),
    2: (0, 2),
    3: (0, 1),
    4: (0, 1, 2),
}


def laser(row, col, dirs, add, board):
    for d in dirs:
        dr, dc = delta[(d + add) % 4]
        nr = row + dr
        nc = col + dc
        while 0 <= nr < N and 0 <= nc < M and board[nr][nc] != 6:
            board[nr][nc] = 9
            nr += dr
            nc += dc


def blankcheck(board):
    cnt = 0
    for r in range(N):
        for c in range(M):
            if not board[r][c]:
                cnt += 1
    return cnt


def DFS(last, path):
    if last == len(cctv) - 1:
        tmpboard = deepcopy(board)
        for type, row, col, add in path:
            laser(row, col, arrow[type], add, tmpboard)
        global minblank
        blank = blankcheck(tmpboard)
        if blank < minblank:
            minblank = blank
        return

    no = last + 1
    type, row, col = cctv[no]
    if type == 2:
        dirs = range(2)
    else:
        dirs = range(4)
    for d in dirs:
        path.append((type, row, col, d))
        DFS(no, path)
        path.pop()


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cctv = []
fives = []
for r in range(N):
    for c in range(M):
        if board[r][c] == 5:
            fives.append((r, c))
        elif board[r][c] and board[r][c] != 6:
            cctv.append((board[r][c], r, c))

for r, c in fives:
    laser(r, c, range(4), 0, board)

minblank = float('inf')
DFS(-1, [])
print(minblank)
