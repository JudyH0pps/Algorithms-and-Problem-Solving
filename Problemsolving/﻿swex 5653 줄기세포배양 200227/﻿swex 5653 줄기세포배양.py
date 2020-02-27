# ﻿swex 5653 줄기세포배양

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
from collections import defaultdict

delta = ((0, 1), (1, 0), (-1, 0), (0, -1))

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    visit = defaultdict(int)

    cells = []
    for r in range(N):
        for c in range(M):
            if board[r][c]:
                visit[r, c] = 1
                cells.append((0, -board[r][c], board[r][c], board[r][c] * 2, r, c))
    heapq.heapify(cells)

    # beforeT = -1
    while cells[0][0] < K:
        # if cells[0][0] != beforeT:
        #     beforeT = cells[0][0]
        #     print(cells)
        time, power, start, end, row, col = heapq.heappop(cells)
        time += 1

        if start < time:
            for dr, dc in delta:
                nr = row + dr
                nc = col + dc
                if not visit[nr, nc]:
                    visit[nr, nc] = 1
                    heapq.heappush(cells, (time, power, time - power, time - power * 2, nr, nc))
        if time < end:
            heapq.heappush(cells, (time, power, start, end, row, col))

    print('#%d' % test_case, len(cells))
