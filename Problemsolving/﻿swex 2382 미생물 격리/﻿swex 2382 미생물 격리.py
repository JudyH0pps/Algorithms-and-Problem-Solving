# ﻿swex 2382 미생물 격리

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
from collections import defaultdict

delta = {
    1: (-1, 0),
    2: (1, 0),
    3: (0, -1),
    4: (0, 1)
}
change = {
    1: 2,
    2: 1,
    3: 4,
    4: 3
}
T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    micro = [list(map(int, input().split())) for _ in range(K)]

    for _ in range(M):
        board = defaultdict(int)
        maxSize = defaultdict(int)
        direction = defaultdict(int)
        for row, col, size, dir in micro:
            dr, dc = delta[dir]
            nr = row + dr
            nc = col + dc
            if nr == 0 or nc == 0 or nr == N - 1 or nc == N - 1:
                size //= 2
                dir = change[dir]
                if not size:
                    continue
            board[nr, nc] += size
            if size > maxSize[nr, nc]:
                maxSize[nr, nc] = size
                direction[nr, nc] = dir
        micro = []
        for roc, size in board.items():
            micro.append((*roc, size, direction[roc[0], roc[1]]))
    # print(micro)
    print('#%d' % test_case, sum(map(lambda x: x[2], micro)))
