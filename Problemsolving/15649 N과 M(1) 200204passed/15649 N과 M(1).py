# 15649 N과 M(1)

import sys
input = sys.stdin.readline

def combination(now, last):
    if last == M:
        print(*now)
        return
    for i in range(1,N+1):
        if chk[i]:
            continue
        nnow = now[:]
        nnow.append(i)
        chk[i] = 1
        combination(nnow, last+1)
        chk[i] = 0

N, M = map(int,input().split())

chk = [0 for _ in range(N+1)]
combination(now = [],last = 0)
