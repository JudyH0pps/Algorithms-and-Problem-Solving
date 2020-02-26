#﻿swex 6485 삼성시의 버스 노선

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

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    busstop = [0] * 5002
    for _ in range(N):
        a, b = map(int,input().split())
        busstop[a] += 1
        busstop[b+1] -= 1
    P = int(input())
    Cs = []
    for _ in range(P):
        Cs.append(int(input()))

    for i in range(1,max(Cs)+1):
        busstop[i] += busstop[i-1]


    print('#%d'%test_case,end=' ')
    for c in Cs:
        print(busstop[c],end=' ')
    print()



