# ﻿swex 2477 차량 정비소

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

T = int(input())

for test_case in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())
    receptionTime = tuple(map(int, input().split()))
    repairTime = tuple(map(int, input().split()))
    client = tuple(map(int, input().split()))

    receptionDesk = [0] * N
    receptionClient = [[] for _ in range(N)]
    receptionWaiting = [0] * N
    repairDesk = [0] * M
    repairClient = [[] for _ in range(M)]
    repairWaiting = [0] * M
    receptionQueue = deque()
    repairQueue = deque()

    time = 0
    ptr = 0
    end = False
    while True:
        for no in range(N):
            receptionDesk[no] >>= 1
            if receptionDesk[no] == 0 and receptionWaiting[no]:
                repairQueue.append(receptionWaiting[no])
                receptionWaiting[no] = 0
        for no in range(M):
            repairDesk[no] >>= 1
            if repairDesk[no] == 0 and repairWaiting[no]:
                if repairWaiting[no] == K:
                    end = True
                repairWaiting[no] = 0
        if end:
            break

        for no in range(M):
            if not repairQueue:
                break
            if not repairWaiting[no]:
                repairWaiting[no] = repairQueue.popleft()
                repairClient[no].append(repairWaiting[no])
                repairDesk[no] = 1 << (repairTime[no] - 1)

        while ptr < K and client[ptr] == time:
            receptionQueue.append(ptr + 1)
            ptr += 1

        for no in range(N):
            if not receptionQueue:
                break
            if not receptionWaiting[no]:
                receptionWaiting[no] = receptionQueue.popleft()
                receptionClient[no].append(receptionWaiting[no])
                receptionDesk[no] = 1 << (receptionTime[no] - 1)

        # print(time, receptionWaiting, repairWaiting)
        # print(receptionDesk, repairDesk)
        # print(receptionQueue, repairQueue)
        time += 1

    answer = sum(set(receptionClient[A - 1]) & set(repairClient[B - 1]))
    if not answer:
        answer = -1
    print('#%d' % test_case, answer)
