import sys

sys.stdin = open('input.txt', 'r')

import heapq
from collections import defaultdict


def printB(board):
    print()
    for i in range(R):
        for j in range(C):
            if board[i][j]:
                p = board[i][j][0]
            else:
                p = "'"
            print(p, end=' ')
        print()
    print()


delta = (
    (-1, 0),  # 위
    (1, 0),  # 아래
    (0, 1),  # 오른쪽
    (0, -1),  # 왼쪽
)

R, C, M = map(int, input().split())

caught_size = 0
sharks = []
board = [[0] * C for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r - 1][c - 1] = (s, d - 1, z)


for king in range(C):
    for land_level in range(R):
        if board[land_level][king]:
            caught_size += board[land_level][king][2]
            board[land_level][king] = 0
            break

    new_board = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if not board[r][c]:
                continue
            s, d, z = board[r][c]
            original_s = s
            board[r][c] = 0
            dr, dc = delta[d]
            dr = dr * s
            dc = dc * s
            nr = r
            nc = c
            if d == 0:
                # print('위')
                if s <= r:
                    nr = r + dr
                else:
                    s -= r
                    f = s // (R - 1)
                    s %= (R - 1)
                    if f % 2:
                        nr = R - 1 - s
                        d = 0
                    else:
                        nr = s
                        d = 1
            elif d == 1:
                # print('아래')
                if s <= (R - r - 1):
                    nr = r + dr
                else:
                    s -= (R - r - 1)
                    f = s // (R - 1)
                    s %= (R - 1)
                    if f % 2:
                        nr = s
                        d = 1
                    else:
                        nr = (R - s - 1)
                        d = 0
            elif d == 2:
                # print('오른쪽')
                if s <= (C - c - 1):
                    nc = c + dc
                else:
                    s -= (C - c - 1)
                    f = s // (C - 1)
                    s %= (C - 1)
                    if f % 2:
                        nc = s
                        d = 2
                    else:
                        nc = C - 1 - s
                        d = 3

            elif d == 3:
                # print('왼쪽')
                if s <= c:
                    nc = c + dc
                else:
                    s -= c
                    f = s // (C - 1)
                    s %= (C - 1)
                    if f % 2:
                        nc = C - 1 - s
                        d = 3
                    else:
                        nc = s
                        d = 2

            # print(r, c, '-->', nr, nc)
            if (new_board[nr][nc] and z > new_board[nr][nc][2]) or not new_board[nr][nc]:
                new_board[nr][nc] = (original_s, d, z)

    # print('후')
    board = new_board
    # printB(board)

print(caught_size)