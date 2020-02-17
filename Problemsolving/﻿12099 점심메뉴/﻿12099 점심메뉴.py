#﻿12099 점심메뉴

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

N,Q = map(int,input().split())
dish = [0]*N
for i in range(N):
    a,b = map(int,input().split())
    dish[i] = (a,b)

booard = [0]*1000000001
for _ in range(Q):
    astart,aend,bstart,bend = map(int,input().split())


