# ﻿swex 2819 격자판의 숫자 이어 붙이기

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

def DFS(row, col, level):
    for dr, dc in delta:
        nr = row + dr
        nc = col + dc
        if 0 <= nr < 4 and 0 <= nc < 4:
            path[level + 1] = board[nr][nc]
            if level == 5:
                # print(path)
                nums.add(tuple(path))
                continue
            DFS(nr, nc, level + 1)


delta = ((0, 1), (1, 0), (-1, 0), (0, -1))

T = int(input())
for test_case in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(4)]
    nums = set()
    path = [0] * 7


    for r in range(4):
        for c in range(4):
            path[0] = board[r][c]
            DFS(r, c, 0)

    print('#%d' % test_case, len(nums))
