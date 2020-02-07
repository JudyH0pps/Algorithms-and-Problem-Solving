#﻿swex 1493 수의 새로운 연산

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

base = [x for x in range(10001)]
cumulSum = [0 for _ in range(20000)]
for i in range(1,10001):
    cumulSum[i] = cumulSum[i-1] + base[i]


def board(x,y):
    p = cumulSum[x+y-1] - y + 1
    dic[p] = (x,y)
    return p

dic = {}
def ampersenc(p):
    if p in dic:
        return dic[p]
    nowx = 0
    nowy = 1
    nowp = -1
    while nowp < p :
        nowx += 1
        nowp = board(nowx,nowy)
    diff = nowp - p
    return nowx - diff ,nowy + diff

T = int(input())

for test_case in range(1,T+1):
    p, q = list(map(int,input().split()))
    px,py = ampersenc(p)
    qx,qy = ampersenc(q)
    print('#%d'%test_case,board(px+qx,py+qy))
