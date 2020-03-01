# ﻿4179 불!

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
import heapq


def printB(board):
    for i in range(R):
        for c in range(C):
            print(board[i][c], end=' ')
        print()
    print()


def init(board):
    q = []
    for r in range(R):
        for c in range(C):
            if board[r][c] == 'J':
                heapq.heappush(q, (0, 1, r, c))
            elif board[r][c] == 'F':
                board[r][c] = 'F'
                heapq.heappush(q, (0, 0, r, c))
    return q


def BFS(q):
    while q:
        # printB(board)
        level, char, row, col = heapq.heappop(q)

        for dr, dc in delta:
            nr = row + dr
            nc = col + dc
            if not (0 <= nr < R and 0 <= nc < C):
                if char == 1:
                    return level + 1
                continue
            if board[nr][nc] == '.':
                if char == 1:
                    board[nr][nc] = 'J'
                else:
                    board[nr][nc] = 'F'
                heapq.heappush(q, (level + 1, char, nr, nc))

    return 'IMPOSSIBLE'


delta = ((0, 1), (1, 0), (-1, 0), (0, -1))

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
q = init(board)
print(BFS(q))
