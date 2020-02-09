#﻿2606 바이러스

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
def findP(x):
    p = parent[x]
    if p == x:
        return p
    else:
        p = findP(p)
        parent[x] = p
        return p
def union(x,y):
    x = findP(x)
    y = findP(y)
    if x != y:
        if x > y:
            parent[x] = y
        else:
            parent[y] = x

N = int(input())
M = int(input())
parent = [i for i in range(N+1)]

for _ in range(M):
    x, y = map(int,input().split())
    union(x,y)

cnt = 0
for i in range(2,N+1):
    if findP(i) == 1:
        cnt += 1

print(cnt)