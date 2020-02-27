# ﻿swex 2117 홈 방범 서비스

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
from collections import defaultdict, deque

delta = ((0, 1), (1, 0), (0, -1), (-1, 0))


def BFS(row, col, K):
    homecnt = 0
    visit = defaultdict(int)
    visit[row, col] = 1
    q = deque()
    q.append((row, col, 1))
    while q:
        row, col, level = q.popleft()
        if board[row][col]:
            homecnt += 1
        if level >= K:
            continue
        for i in range(4):
            dr, dc = delta[i]
            nr = row + dr
            nc = col + dc
            if 0 <= nr < N and 0 <= nc < N and not visit[nr, nc]:
                visit[nr, nc] = 1
                q.append((nr, nc, level + 1))
    return homecnt


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    home = 0
    for r in range(N):
        for c in range(N):
            if board[r][c]:
                home += 1
    K = 1
    maxcnt = -1
    while home * M >= K ** 2 + (K - 1) ** 2:
        cost = K ** 2 + (K - 1) ** 2
        for r in range(N):
            for c in range(N):
                homecnt = BFS(r, c, K)
                earning = homecnt * M - cost
                if earning >= 0 and homecnt > maxcnt:
                    # print(K,r,c,homecnt)
                    maxcnt = homecnt
        K += 1

    print('#%d' % test_case, maxcnt)
