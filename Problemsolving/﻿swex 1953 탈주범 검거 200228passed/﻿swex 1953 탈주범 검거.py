# ﻿swex 1953 탈주범 검거

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

# 동남서북
delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
branch = {
    1: (0, 1, 2, 3),
    2: (1, 3),
    3: (0, 2),
    4: (0, 3),
    5: (0, 1),
    6: (1, 2),
    7: (2, 3)
}
moveok = {
    0: (1, 3, 6, 7),  # 동
    1: (1, 2, 4, 7),  # 남
    2: (1, 3, 4, 5),  # 서
    3: (1, 2, 5, 6),  # 북
}


def BFS(row, col):
    cnt = 0
    visit = [[0] * M for _ in range(N)]
    q = deque()
    q.append((row, col, 1))
    visit[row][col] = 1
    cnt += 1
    while q:
        row, col, level = q.popleft()
        level += 1
        for i in branch[board[row][col]]:
            dr, dc = delta[i]
            nr = row + dr
            nc = col + dc
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] and not visit[nr][nc] and board[nr][nc] in moveok[i]:
                cnt += 1
                visit[nr][nc] = 1
                if level >= L:
                    continue
                q.append((nr, nc, level))
    return cnt


T = int(input())
for test_case in range(1, T + 1):
    print('#%d' % test_case, end=' ')
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    if L == 1:
        print(1)
        continue

    print(BFS(R, C))
