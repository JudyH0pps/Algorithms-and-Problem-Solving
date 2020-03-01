# 16436 얼룩말아트

############# 입력모드
# 0 : txt 모드 1: 제출

INPUTMODE = 0
if not INPUTMODE:
    f = open("input.txt", "r")
    input = f.readline
else:
    import sys

    input = lambda: sys.stdin.readline().rstrip()
##################################
W, H, K = map(int, input().split())
board1 = [[0 for _ in range(W + 2)] for _ in range(H + 2)]
board2 = [[0 for _ in range(W + 4)] for _ in range(H + 4)]

for _ in range(K):
    figure = tuple(map(int, input().split()))
    if figure[0] == 1:
        _, px, py, qx, qy = figure
        board1[py + 1][px + 1] += 1
        board1[py + 1][qx + 2] -= 1
        board1[qy + 2][px + 1] -= 1
        board1[qy + 2][qx + 2] += 1
    else:
        _, px, py, r = figure
        py += 2
        px += 2
        board2[py + 1 - r][px] += 1
        board2[py - r][px] += 1
        board2[py + 1][px + 1 + r] -= 1
        board2[py + 1][px + r] -= 1
        board2[py + 1][px - r - 1] -= 1
        board2[py + 1][px - r] -= 1
        board2[py + r + 1][px] += 1
        board2[py + r + 2][px] += 1

for r in range(1, H + 3):
    for c in range(1, W + 3):
        if r < H + 2 and c < W + 2:
            board1[r][c] += board1[r][c - 1] + board1[r - 1][c] - board1[r - 1][c - 1]
        board2[r + 1][c] += board2[r + 1 - 1][c + 1] + board2[r + 1 - 1][c - 1] - board2[r + 1 - 2][c]


for r in range(H):
    for c in range(W):
        now = board1[r + 1][c + 1] + board2[r + 2][c + 2]
        if now % 2 == 0:
            print('.', end='')
        else:
            print('#', end='')
    print()
