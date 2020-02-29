# ﻿swex 1225 암호 생성기

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

for _ in range(10):
    test_case = int(input())
    nums = list(map(int, input().split()))
    ptr = -1
    sub = -1
    while nums[ptr] > 0:
        ptr = (ptr + 1) % 8
        sub = (sub + 1) % 5
        nums[ptr] -= sub + 1
    ptr = (ptr + 1) % 8
    nums[ptr-1] = 0

    print('#%d' % test_case, end=' ')
    for _ in range(8):
        print(nums[ptr], end=' ')
        ptr = (ptr + 1) % 8
    print()
