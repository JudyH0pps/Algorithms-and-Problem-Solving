# ﻿3197 백조의 호수

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
from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)

# def findP(r, c):
#     nowP = parent[r][c]
#     if (r, c) == nowP:
#         return nowP
#
#     P = findP(*nowP)
#     parent[r][c] = P
#     return P
#
#
# def union(r1, c1, r2, c2):
#     p1 = findP(r1, c1)
#     p2 = findP(r2, c2)
#
#     if p1 < p2:
#         parent[p2[0]][p2[1]] = p1
#     else:
#         parent[p1[0]][p1[1]] = p2

def printB(board):
    for r in range(R):
        for c in range(C):
            print(board[r][c], end=' ')
        print()
    print()


def DFS(pr, pc, row, col):
    for dr, dc in delta:
        nr = row + dr
        nc = col + dc
        if not (0 <= nr < R and 0 <= nc < C) or visit[nr][nc]:
            continue
        if board[nr][nc] == 'X':
            visit[nr][nc] = 1
            q.append((nr, nc))

        elif board[nr][nc] == '.':
            visit[nr][nc] = 1
            DFS(pr, pc, nr, nc)

delta = ((0, 1), (1, 0), (-1, 0), (0, -1))

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visit = [[0] * C for _ in range(R)]

q = deque()

find = False

bird = [0] * 2


def findBird():
    n = 0
    for r in range(R):
        for c in range(C):
            if board[r][c] == 'L':
                bird[n] = (r, c)
                board[r][c] = '.'
                if n == 1:
                    return
                n += 1


def init():
    for r in range(R):
        for c in range(C):
            if not visit[r][c] and board[r][c] == '.':
                visit[r][c] = 1
                DFS(r, c, r, c)


findBird()
init()


printB(board)
printB(visit)
# printB(parent)


if findP(*bird[0]) == findP(*bird[1]):
    print(0)

else:
    def BFS():
        level = 1
        while q:
            visit = [[0] * C for _ in range(R)]
            toNextLevel = len(q)
            for _ in range(toNextLevel):
                row, col = q.popleft()
                board[row][col] = '.'

                for dr, dc in delta:
                    nr = row + dr
                    nc = col + dc
                    if not (0 <= nr < R and 0 <= nc < C):
                        continue

                    if board[nr][nc] == '.':
                        union(row, col, nr, nc)

                    elif not visit[nr][nc]:
                        visit[nr][nc] = 1
                        q.append((nr, nc))

            printB(board)
            # printB(parent)
            # print(findP(*bird[0]), findP(*bird[1]))
            if findP(*bird[0]) == findP(*bird[1]):
                return level
            level += 1

    print(BFS())
