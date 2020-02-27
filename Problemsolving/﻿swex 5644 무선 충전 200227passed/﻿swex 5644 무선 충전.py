# ﻿swex 5644 무선 충전

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
from itertools import product

delta = ((0, 0), (0, -1), (1, 0), (0, 1), (-1, 0))


def BFS(x, y, vision, no):
    charger[no].append((x, y))
    q = deque()
    q.append((x, y, 0))
    while q:
        x, y, level = q.popleft()
        level += 1
        for i in range(1, 5):
            dx, dy = delta[i]
            nx = x + dx
            ny = y + dy
            if 1 <= nx < 11 and 1 <= ny < 11 and not (nx, ny) in charger[no]:
                charger[no].append((nx, ny))
                if level >= vision:
                    continue
                q.append((nx, ny, level))


def move(x, y, dir):
    dx, dy = delta[dir]
    x += dx
    y += dy
    return x, y


def connect(one, two):
    if one == two:
        return chargerP[one]
    else:
        return chargerP[one] + chargerP[two]


T = int(input())
for test_case in range(1, T + 1):
    M, A = map(int, input().split())
    amove = list(map(int, input().split()))
    bmove = list(map(int, input().split()))
    ax, ay, bx, by = 1, 1, 10, 10
    T = [0] * (M + 1)
    charger = [[] for _ in range(A)]
    chargerP = [0] * A
    for i in range(A):
        x, y, vision, power = map(int, input().split())
        BFS(x, y, vision, i)
        chargerP[i] = power

    for t in range(M + 1):
        achar = []
        bchar = []
        for i in range(A):
            if (ax, ay) in charger[i]:
                achar.append(i)
            if (bx, by) in charger[i]:
                bchar.append(i)
        if not achar and not bchar:
            result = 0
        elif not achar:
            result = max(list(map(lambda x: chargerP[x], bchar)))
        elif not bchar:
            result = max(list(map(lambda x: chargerP[x], achar)))
        else:
            maxR = -1
            for x in product(achar, bchar):
                maxR = max(maxR, connect(*x))
            result = maxR

        T[t] = result
        # print(t, achar, bchar)
        if t >= M:
            break
        ax, ay = move(ax, ay, amove[t])
        bx, by = move(bx, by, bmove[t])
    print('#%d' % test_case, sum(T))
