# ﻿swex 1861 정사각형 방

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

delta = ((0, 1), (1, 0), (-1, 0), (0, -1))
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]

    start = 10 ** 7
    maxL = -1
    for r in range(N):
        for c in range(N):
            if not visit[r][c]:
                visit[r][c] = 1
                stack = []
                stack.append((r, c))
                left = board[r][c]
                right = board[r][c]
                while stack:
                    row, col = stack.pop()
                    if board[row][col] > right:
                        right = board[row][col]
                    elif board[row][col] < left:
                        left = board[row][col]

                    for dr, dc in delta:
                        nr = row + dr
                        nc = col + dc
                        if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc]:
                            if abs(board[row][col] - board[nr][nc]) == 1:
                                visit[nr][nc] = 1
                                stack.append((nr, nc))
                # print(left,right)
                if maxL < right - left or (maxL == right - left and start > left):
                    start = left
                    maxL = right - left

    print('#%d' % test_case, start, maxL+1)
