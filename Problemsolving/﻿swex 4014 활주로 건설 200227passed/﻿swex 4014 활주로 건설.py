# ﻿swex 4014 활주로 건설

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
from itertools import chain, combinations


def install(road, slides):
    tmp = [0] * len(road)
    visit = [0] * len(road)

    for slide in slides:
        if visit[abs(slide)]:
            return False
        if slide > 0:
            tmp[slide] += 1
            left = slide
            right = slide + X
        else:
            slide *= -1
            tmp[0] += 1
            tmp[slide+1] -= 1
            left = slide - X + 1
            right = slide + 1

        for i in range(left, right):
            if visit[i]:
                return False
            visit[i] = 1

    for i in range(1,len(road)):
        tmp[i] += tmp[i-1]
    for i in range(len(road)):
        tmp[i] += road[i]

    # print(road,slides)
    # print(tmp)
    height = tmp[0]
    for i in range(1, len(road)):
        if tmp[i] != height:
            return False
    # print('T')
    return True


def check(road):
    slide = []
    for i in range(1, len(road) - 1):
        if abs(road[i] - road[i + 1]) >= 2 or abs(road[i] - road[i - 1]) >= 2:
            return 0
        # 우하향 체크
        if road[i:i + X] == [road[i]] * X and road[i - 1] == road[i] + 1:
            slide.append(i)
        # 우상향 체크
        if road[i - X + 1:i + 1] == [road[i]] * X and road[i + 1] == road[i] + 1:
            slide.append(-i)

    for perm in chain.from_iterable(combinations(slide, r) for r in range(len(slide) + 1)):
        if install(road, perm):
            # print(TTTT')
            return 1
    return 0


T = int(input())
for test_case in range(1, T + 1):
    N, X = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    # print('garo')
    for line in board:
        cnt += check(line)
    # print('sero')
    for line in zip(*board):
        cnt += check(list(line))

    print('#%d' % test_case, cnt)
