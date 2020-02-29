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


def printB(board):
    for i in range(N):
        for j in range(M):
            print(board[i][j], end=' ')
        print()
    print()


N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

delta = ((0, 1), (1, 0), (-1, 0), (0, -1))


def BFS():
    visit = [[0] * M for _ in range(N)]
    afterbreak = [[0] * M for _ in range(N)]
    q = deque()
    broke, row, col, level = 0, 0, 0, 1
    q.append((broke, level, row, col))
    visit[row][col] = 1
    while q:
        broke, level, row, col = q.popleft()
        for dr, dc in delta:
            nr = row + dr
            nc = col + dc
            if 0 <= nr < N and 0 <= nc < M:
                if not broke and (not visit[nr][nc] or visit[nr][nc] > level + 1):
                    visit[nr][nc] = level + 1
                    if board[nr][nc]:
                        if (nr,nc) == (N-1,M-1):
                            return level + 1
                        q.append((1, level + 1, nr, nc))
                    elif not board[nr][nc]:
                        if (nr,nc) == (N-1,M-1):
                            return level + 1
                        q.append((0, level + 1, nr, nc))
                elif broke and not board[nr][nc] and (not afterbreak[nr][nc] or afterbreak[nr][nc] > level + 1):
                    if (nr, nc) == (N - 1, M - 1):
                        return level + 1
                    afterbreak[nr][nc] = level + 1
                    q.append((1, level + 1, nr, nc))
    return -1

if (N,M) == (1,1):
    print(1)
else:
    print(BFS())
