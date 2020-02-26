#﻿swex 1249 보급로

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt","r")
    input = lambda : f.readline().rstrip()
else:
    import sys
    input = lambda : sys.stdin.readline().rstrip()
################################

import heapq


def printB(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()
    print()


def isWall(row, col):
    if 0 <= row < N and 0 <= col < N:
        return False
    return True


delta = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1)
]


def BFS(distance, row, col):
    q = []
    heapq.heappush(q, (distance, row, col))
    while q:
        distance, row, col = heapq.heappop(q)
        for i in range(4):
            dr, dc = delta[i]
            nr = row + dr
            nc = col + dc
            if isWall(nr, nc):
                continue
            next = board[nr][nc]

            if chk[nr][nc] == 10000 or distance + next < chk[nr][nc]:
                chk[nr][nc] = distance + next
                if (nr, nc) == (N - 1, N - 1):
                    return
                heapq.heappush(q, (distance + next, nr, nc))
            else:
                continue


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    chk = [[10000] * N for _ in range(N)]

    BFS(0, 0, 0)
    # printB(chk)
    print('#%d' % test_case, chk[N - 1][N - 1])