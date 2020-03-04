# ﻿swex 8382 방향 전환

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
    a, b, c, d = map(int, input().split())
    x = abs(c - a)
    y = abs(d - b)
    ans = min(x,y) * 2
    line = abs(x-y)
    if line:
        ans += (line // 2) * 4 + line % 2
    print('#%d'%test_case,ans)
