# ﻿2003 스티커 붙이기

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
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=' ')
        print()
    print()


def clockwise(sticker):
    R = len(sticker[0])
    C = len(sticker)
    new = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            new[r][c] = sticker[C - c - 1][r]

    # printB(sticker)
    # printB(new)
    return new


def chk(sticker):
    def test(sticker):
        for tr in range(r, r + R):
            for tc in range(c, c + C):
                if board[tr][tc] == 1 and sticker[tr - r][tc - c] == 1:
                    return False
        return True

    for r in range(N - R + 1):
        for c in range(M - C + 1):
            if test(sticker):
                for tr in range(r, r + R):
                    for tc in range(c, c + C):
                        board[tr][tc] |= sticker[tr - r][tc - c]
                return True
    return False


N, M, K = map(int, input().split())

board = [[0] * M for _ in range(N)]

for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]

    for _ in range(4):
        # print('now')
        # printB(sticker)
        if chk(sticker):
            # printB(board)
            # print('OK')
            break
        else:
            sticker = clockwise(sticker)
            R, C = C, R

ans = 0
for r in range(N):
    for c in range(M):
        if board[r][c]:
            ans += 1

printB(board)
print(ans)


