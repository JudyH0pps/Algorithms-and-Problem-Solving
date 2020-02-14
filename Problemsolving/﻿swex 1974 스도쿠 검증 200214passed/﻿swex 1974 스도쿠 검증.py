# ﻿swex 1974 스도쿠 검증

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
from itertools import product

T = int(input())
for test_case in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(9)]


    def sudokuchk(board):
        for r in range(9):
            nums = defaultdict(int)
            for c in range(9):
                if nums[board[r][c]] == 1:
                    return False
                nums[board[r][c]] += 1
        for c in range(9):
            nums = defaultdict(int)
            for r in range(9):
                if nums[board[r][c]] == 1:
                    return False
                nums[board[r][c]] += 1
        for sr, sc in product((0, 3, 6), (0, 3, 6)):
            nums = defaultdict(int)
            for r in range(sr, sr + 3):
                for c in range(sc, sc + 3):
                    if nums[board[r][c]] == 1:
                        return False
                    nums[board[r][c]] += 1
        return True


    if sudokuchk(board):
        print('#%d' % test_case, 1)
    else:
        print('#%d' % test_case, 0)
