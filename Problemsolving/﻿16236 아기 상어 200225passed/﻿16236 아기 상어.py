# ﻿16236 아기 상어

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

delta = (
    (-1, 0),
    (0, -1),
    (0, 1),
    (1, 0)
)


def findFish(row, col):
    visit = [[0] * N for _ in range(N)]
    q = []
    heapq.heappush(q,(0, row, col))
    while q:
        # print(q)
        time, row, col = heapq.heappop(q)
        if 0 < board[row][col] < size:
            board[row][col] = 0
            return (row, col), time
        for i in range(4):
            dr, dc = delta[i]
            nr = row + dr
            nc = col + dc
            if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc] and board[nr][nc] <= size:
                visit[nr][nc] = 1
                heapq.heappush(q,(time + 1, nr, nc))


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

size = 2
tabeta = 0
for r in range(N):
    for c in range(N):
        if board[r][c] == 9:
            shark = (r, c)
            board[r][c] = 0
            break

g_time = 0
while True:
    result = findFish(*shark)
    if result:
        shark, time = result
    else:
        break
    tabeta += 1
    g_time += time
    if tabeta >= size:
        tabeta = 0
        size += 1
    # print(shark, time, size, tabeta, g_time)
print(g_time)
