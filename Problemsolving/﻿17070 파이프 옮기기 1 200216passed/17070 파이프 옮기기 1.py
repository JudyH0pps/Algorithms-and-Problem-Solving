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
# 0빈칸 1벽 2가로 3대각선 4세로
def printB(board):
    for i in range(N+1):
        for j in range(N):
            print(board[i][j], end=' ')
        print()
    print()

def isWall(row, col):
    if 0 <= row < N and 0 <= col < N and board[row][col] == 0:
        return False
    return True


def DP():
    for r in range(1,N+1):
        for c in range(2,N):
            if board[r][c]:
                continue
            garo[r][c] = garo[r][c-1] + diag[r][c-1]
            sero[r][c] = sero[r-1][c] + diag[r-1][c]
            if board[r-1][c] or board[r][c-1]:
                continue
            diag[r][c] = garo[r-1][c-1] + sero[r-1][c-1] + diag[r-1][c-1]





N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
board = [[0]*N] + board

garo = [[0]*N for _ in range(N+1)]
sero = [[0]*N for _ in range(N+1)]
diag = [[0]*N for _ in range(N+1)]
garo[1][1] = 1
save = {
    2:garo,
    3:diag,
    4:sero
}

DP()
# printB(garo)
# printB(sero)
# printB(diag)
print(garo[N][N-1] + sero[N][N-1] + diag[N][N-1])