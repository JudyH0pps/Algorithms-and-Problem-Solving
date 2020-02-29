# ﻿swex 1952 수영장

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

T = int(input())
for test_case in range(1, T + 1):
    # 1일, 1달, 3달, 12달
    price = list(map(int, input().split()))
    month = [0] + list(map(int, input().split()))
    for i in range(1, 13):
        day = month[i] * price[0] + month[i - 1]
        mon = price[1] + month[i - 1]
        threemon, year = 3000 * 32, 3000 * 32
        if i >= 3:
            threemon = price[2] + month[i - 3]
        if i >= 12:
            year = price[3] + month[i - 12]
        month[i] = min(day, mon, threemon, year)
    print('#%d' % test_case, month[-1])
