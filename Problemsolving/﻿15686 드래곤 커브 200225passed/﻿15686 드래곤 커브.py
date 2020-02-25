# ﻿15686 드래곤 커브

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
    for i in range(101):
        for j in range(101):
            print(board[i][j],end=' ')
        print()
    print()

delta = (
    (0, 1),  # 동
    (-1, 0),  # 서
    (0, -1),  # 북
    (1, 0)  # 남
)


def drawCurve(col, row, d, gen):
    board[row][col] = 1
    path = [(row, col)]
    dr, dc = delta[d]
    fixr = row + dr
    fixc = col + dc
    board[fixr][fixc] = 1
    for _ in range(gen):
        # print(path)
        for row, col in reversed(path):
            kr = fixr - (fixc - col)
            kc = fixc + (fixr - row)
            board[kr][kc] = 1
            path.append((kr,kc))
        path.append((fixr,fixc))
        fixr = kr
        fixc = kc
        # printB(board)

N = int(input())
board = [[0] * 101 for _ in range(101)]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    drawCurve(x, y, d, g)
count = 0
for r in range(1,101):
    for c in range(1,101):
        if board[r-1][c-1] and board[r][c] and board[r-1][c] and board[r][c-1]:
            count += 1
print(count)
