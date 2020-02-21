# ﻿1388 바닥 장식

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

def printB(board):
    for i in range(N):
        for j in range(M):
            print('%1s' % board[i][j], end=' ')
        print()
    print()


def garo(r, c):
    while 0 <= r < N and 0 <= c < M and board[r][c] == '-':
        board[r][c] = ''
        c += 1


def sero(r, c):
    while 0 <= r < N and 0 <= c < M and board[r][c] == '|':
        board[r][c] = ''
        r += 1


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

cnt = 0
for r in range(N):
    for c in range(M):
        if board[r][c]:
            cnt += 1
            if board[r][c] == '-':
                garo(r, c)
            elif board[r][c] == '|':
                sero(r, c)
print(cnt)