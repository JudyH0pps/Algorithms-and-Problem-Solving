# ﻿17070 파이프 옮기기 1

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
import sys
sys.setrecursionlimit(10**6)
# 0빈칸 1벽 2가로 3대각선 4세로
def printB(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()
    print()

delta = {
    2: (0, 1),
    3: (1, 1),
    4: (1, 0)
}

nextDir = {
    2: (2, 3),
    3: (2, 3, 4),
    4: (3, 4)
}


def isWall(row, col):
    if 0 <= row < N and 0 <= col < N and board[row][col] == 0:
        return False
    return True


def DFS(row, col, direction):
    # printB(row,col,direction)
    dr, dc = delta[direction]
    nr = row + dr
    nc = col + dc
    for dir in nextDir[direction]:
        ndr, ndc = delta[dir]
        nnr = nr + ndr
        nnc = nc + ndc
        if isWall(nnr,nnc) or (dir == 3 and (board[nnr-1][nnc] == 1 or board[nnr][nnc-1]==1)):
            continue
        chk = save[dir]
        chk[nnr][nnc] += 1
        if (nnr,nnc) == (N-1,N-1):
            global cnt
            cnt += 1
            continue
        DFS(nr,nc,dir)


N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
garo = [[0]*N for _ in range(N)]
sero = [[0]*N for _ in range(N)]
diag = [[0]*N for _ in range(N)]
save = {
    2:garo,
    3:diag,
    4:sero
}
cnt = 0
DFS(0, 0, 2)
print(cnt)
# printB(garo)
# printB(sero)
# printB(diag)