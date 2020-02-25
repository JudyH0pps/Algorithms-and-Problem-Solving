# ﻿12099 점심메뉴

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

N, Q = map(int, input().split())

dish = []
for _ in range(N):
    kara, ama = map(int, input().split())
    dish.append((kara, ama))

gugan = []
for _ in range(Q):
    u, v, x, y = map(int, input().split())
    gugan.append((u, v, x, y))
    if v > karamax:
        karamax = v
    if y > amamax:
        amamax = y
