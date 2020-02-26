#﻿swex 2383 모의 SW 점심 식사시간

#####입력 모드
# 0 : txt모드 , 1: 제출용
INPUTMODE = 0

if not INPUTMODE:
    f = open("input.txt","r")
    input = lambda : f.readline().rstrip()
else:
    import sys
    input = lambda : sys.stdin.readline().rstrip()
################################

from collections import deque

debug = 0

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]

    minTime = 1000000

    people = []
    stairs = []
    pCnt = 0
    for r in range(N):
        for c in range(N):
            now = board[r][c]
            if now == 1:
                #사람
                people.append((r,c))
                pCnt += 1
            elif now:
                #계단
                stairs.append((r,c,now))

    dist = [[[] for _ in range(len(people))] for _ in range(2)]

    for i in range(len(people)):
        r,c = people[i]
        for j in range(2):
            sr , sc, _ = stairs[j]
            dist[j][i] = abs(r - sr) + abs(c - sc)

    for n in range(1 << pCnt):
        set = bin(n)[2:].zfill(pCnt)
        first = []
        second = []
        for i in range(pCnt):
            now = set[i]
            if now == '0':
                first.append(dist[0][i])
            elif now == '1':
                second.append(dist[1][i])
        first.sort(reverse=True)
        second.sort(reverse = True)
        # print(second)
        # print(first)

        def out(people, length):
            if debug:
                print(people)
            if not people:
                return 0

            q = deque()
            t = 1
            while True:

                if debug:
                    print(t,q)
                while q:
                    if q[0] + length <= t :
                        q.popleft()
                    else:
                        break
                if not q and not people:
                    break

                while len(q) < 3:
                    if people and people[-1] <= t:
                        x = people.pop()
                        q.append(t)
                    else:
                        break
                t += 1
            return t + 1
        if debug:
            print('@@@@@set@@@@')
        t1 = out(first, stairs[0][2])
        # print(t1)
        t2 = out(second, stairs[1][2])
        # print(t2)
        mint = max(t1,t2)
        if mint < minTime:
            if debug:
                print('chan',mint,t1,t2)
            minTime = mint
    print('#%d'%test_case,minTime)


