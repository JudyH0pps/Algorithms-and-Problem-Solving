# ﻿swex 1268 최종평가

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

def GCD(p, q):
    if p < q:
        return GCD(q, p)
    elif q == 0:
        return p
    else:
        return GCD(q, p % q)


T = int(input())
for tc in range(1, T + 1):
    R, N, K = map(int, input().split())

    # 0안죽음 1죽음 -1아직 안구함
    kill = [[-1] * N for _ in range(N)]

    robots = [tuple(map(int, input().split())) for _ in range(N)]

    for shooter in range(N):
        for target in range(N):
            if shooter == target:
                kill[shooter][target] = 0
            else:
                sr, sc = shooter
                tr, tc = target
                r = GCD(abs(sr),abs(tr))
                s = GCD(abs(sc),abs(tc))
                
