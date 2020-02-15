# ﻿17406 배열 돌리기 4

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
            print(board[i][j], end=' ')
        print()
    print()


def counterrotate(R, C, S):
    R -= 1
    C -= 1
    r1, c1 = R - S, C - S
    r2, c2 = R + S, C + S
    for _ in range(S):
        for c in range(c1, c2):
            board[r1][c], board[r1][c + 1] = board[r1][c + 1], board[r1][c]
        for r in range(r1, r2):
            board[r][c2], board[r + 1][c2] = board[r + 1][c2], board[r][c2]
        for c in range(c2, c1, -1):
            board[r2][c], board[r2][c - 1] = board[r2][c - 1], board[r2][c]
        for r in range(r2, r1 + 1, -1):
            board[r][c1], board[r - 1][c1] = board[r - 1][c1], board[r][c1]
        r1 += 1
        c1 += 1
        r2 -= 1
        c2 -= 1


def clockrotate(R, C, S):
    R -= 1;
    C -= 1
    r1, c1 = R - S, C - S
    r2, c2 = R + S, C + S
    for _ in range(S):
        for r in range(r1, r2):
            board[r][c1], board[r + 1][c1] = board[r + 1][c1], board[r][c1]
        for c in range(c1, c2):
            board[r2][c], board[r2][c + 1] = board[r2][c + 1], board[r2][c]
        for r in range(r2, r1, -1):
            board[r][c2], board[r - 1][c2] = board[r - 1][c2], board[r][c2]
        for c in range(c2, c1 + 1, -1):
            board[r1][c], board[r1][c - 1] = board[r1][c - 1], board[r1][c]
        r1 += 1
        c1 += 1
        r2 -= 1
        c2 -= 1


def summ(board):
    minSum = 10000
    for i in range(N):
        minSum = min(minSum, sum(board[i]))
    return minSum


def permutations(level,path):
    if level == K:
        # printB(board)
        # print(path)
        global minCumul
        # print(summ(board))
        minCumul = min(summ(board), minCumul)
        return
    for i in range(K):
        if visit[i]:
            continue
        clockrotate(*move[i])
        visit[i] = 1
        path.append(i)
        permutations(level + 1,path)
        path.remove(i)
        visit[i] = 0
        counterrotate(*move[i])


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
move = [tuple(map(int, input().split())) for _ in range(K)]
visit = [0] * K

minCumul = 10000000
permutations(0,[])
print(minCumul)
