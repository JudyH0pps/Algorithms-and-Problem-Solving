#﻿swex 7988 내전 경기

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

T = int(input())

for test_case in range(1,T+1):
    K = int(input())
    A = []
    B = []
    opposite = []
    for _ in range(K):
        opposite.append(tuple(input().split()))
    a,b = opposite.pop()
    A.append(a)
    B.append(b)
    nextq = deque(opposite)
    def solve(nextq):
        while nextq:
            nowq = nextq
            nextq = deque()
            for a,b in nowq:
                if (a in A and b in A) or (a in B and b in B):
                    return False
                elif (a in A and b in B) or (a in B and a in A):
                    continue
                elif a in A:
                    B.append(b)
                elif a in B:
                    A.append(b)
                elif b in A:
                    B.append(b)
                elif b in B:
                    A.append(a)
                else:
                    nextq.append((a,b))
            if nowq == nextq:
                break
        return True

    if solve(nextq):
        print('#%d'%test_case,'Yes')
    else:
        print('#%d'%test_case,'No')

