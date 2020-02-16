# ﻿1022 소용돌이 예쁘게 출력하기

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

def printB(board,maxL):
    for i in range(sero):
        for j in range(garo):
            print(board[i][j].rjust(maxL,' '),end=' ')
        print()
r1, c1, r2, c2 = map(int, input().split())
sero = r2-r1+1
garo = c2-c1+1
board = [[0] * (garo) for _ in range(sero)]

maxLeng = -1
for r in range(r1, r2 + 1):
    for c in range(c1, c2 + 1):
        x = max(abs(r), abs(c))
        pivot = (2 * x + 1) ** 2
        # print(pivot)

        def findCnt():
            baseR, baseC = x, x
            # print(r,c, baseR, baseC)
            cnt = 0
            if (baseR, baseC) == (r, c):
                return cnt
            while -x < baseC:
                # print(baseR,baseC)
                if (baseR, baseC) == (r, c):
                    return cnt
                baseC -= 1
                cnt += 1
            while -x < baseR:
                # print(baseR, baseC)
                if (baseR, baseC) == (r, c):
                    return cnt
                baseR -= 1
                cnt += 1
            while x > baseC:
                # print(baseR, baseC)
                if (baseR, baseC) == (r, c):
                    return cnt
                baseC += 1
                cnt += 1
            while x > baseR:
                # print(baseR, baseC)
                if (baseR, baseC) == (r, c):
                    return cnt
                baseR += 1
                cnt += 1

        cnt = findCnt()
        now = str(pivot - cnt)
        maxLeng = max(len(now),maxLeng)
        board[r-r1][c-c1] = now

printB(board,maxLeng)