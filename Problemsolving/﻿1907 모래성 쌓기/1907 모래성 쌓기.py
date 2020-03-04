# ﻿1907 모래성 쌓기

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
    for r in range(N):
        for c in range(M):
            print(board[r][c], end=' ')
        print()
    print()


delta = ((0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1))

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        line = input()
        line = line.replace('.', '0')
        board.append(list(map(int, line)))

    # 무너지는 모래 저장하는 리스트
    # printB(board)
    nextremoved = []
    for r in range(N):
        for c in range(M):
            # 견고함 9인 모래는 절대로 무너지지 않으므로 제외
            if not board[r][c]:
                for dr, dc in delta:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < N and 0 <= nc < M and board[nr][nc] > 0:
                        board[nr][nc] -= 1
                        if not board[nr][nc]:
                            board[nr][nc] = -1
                            nextremoved.append((nr, nc))

    # printB(board)
    # print(nextremoved)

    wave = 0
    # 각 파도마다 실행되는 루프
    while nextremoved:
        wave += 1
        removed = nextremoved
        nextremoved = []

        for r, c in removed:
            for dr, dc in delta:
                nr = r + dr
                nc = c + dc
                if board[nr][nc]:
                    board[nr][nc] -= 1
                    if not board[nr][nc]:
                        nextremoved.append((nr, nc))
        # printB(board)
        # print(nextremoved)

    print('#%d' % test_case, wave)
