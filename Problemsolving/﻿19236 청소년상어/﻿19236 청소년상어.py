# ﻿19236 청소년상어

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

dir = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
)

board = [[0] * 4 for _ in range(4)]

for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        board[i][j] = (line[2 * j], line[2 * j + 1])



