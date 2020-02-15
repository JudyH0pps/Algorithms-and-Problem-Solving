# ﻿1005 ACM craft

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


def build(num):
    maxTime = 0
    for parent in reverseBO[num]:
        now = buildComplete[parent - 1]
        if now < 0:
            now = build(parent)
        maxTime = max(maxTime, now)
    buildComplete[num - 1] = maxTime + buildTime[num - 1]
    return maxTime + buildTime[num - 1]


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    buildTime = tuple(map(int, input().split()))
    reverseBO = defaultdict(list)
    for _ in range(K):
        start, end = map(int, input().split())
        reverseBO[end].append(start)
    W = int(input())
    buildComplete = [-1] * N
    x = build(W)
    print(x)
    # print(buildComplete)
